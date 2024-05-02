# versao alternativa do 'app.py' que usa variáveis de ambiente
from flask import Flask, jsonify
from random import randint
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

@app.route('/quotes')
def index():
    id = randint(0,1000);
    cursor.execute("SELECT * FROM quotes where id = " + str(id) + ";");
    rows = cursor.fetchall()
    #print(rows[0]);

    quote = {
        "autor":rows[0][1],
        "quote":rows[0][2]
    }

    return jsonify(quote);

app.run(host='0.0.0.0', port=8080,debug=True);