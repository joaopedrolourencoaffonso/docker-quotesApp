import json
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="quotesApp",
    password="senha",
    database="quotesApp"
)

cursor = db.cursor()

# Read the JSON file
with open('citacoes.json', 'r') as file:
    quotes_data = json.load(file)

# Insert quotes into the table
for quote in quotes_data:
    author = quote["autor"]
    text = quote["frase"]

    cursor.execute("INSERT INTO quotes (author, quote) VALUES (%s, %s)", (author, text))

# Commit the changes and close the connection
db.commit()
db.close()

