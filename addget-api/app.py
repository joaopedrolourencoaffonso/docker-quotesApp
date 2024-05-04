# versao alternativa do 'app.py' que usa variáveis de ambiente
from flask import Flask, jsonify, request
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of an environment variable
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Connect to the MySQL database
db = mysql.connector.connect(
    host=DATABASE_HOST,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    database=DATABASE_NAME,
    port=3306
)

cursor = db.cursor()


app = Flask(__name__)

@app.route('/addQuote', methods=['POST'])
def add_quote():
    data = request.json
    author = data.get('author')
    quote = data.get('quote')

    # Insert the new quote into the database
    cursor.execute("INSERT INTO quotes (author, quote) VALUES (%s, %s)", (author, quote))
    db.commit()

    # Get the ID of the newly inserted quote
    new_id = cursor.lastrowid

    # Return the ID of the new quote
    return jsonify({'id': new_id,'message':"Nova citação adicionada!"})

@app.route('/getQuote/<int:id>', methods=['GET'])
def get_quote(id):
    cursor.execute("SELECT * FROM quotes WHERE id = " + str(id))
    row = cursor.fetchone()
    
    if row:
        quote = {
            "author": row[1],
            "quote": row[2]
        }
        return jsonify(quote)
    else:
        return jsonify({"message": "A citação não foi encontrada"})

app.run(host='0.0.0.0', port=8080, debug=True)
