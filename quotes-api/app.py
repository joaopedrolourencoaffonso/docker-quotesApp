from flask import Flask, jsonify
from random import randint
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="database",
    user="quotesApp",
    password="senha",
    database="quotesApp",
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
