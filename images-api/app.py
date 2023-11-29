from flask import Flask, send_file
from random import randint


app = Flask(__name__)

@app.route('/imagemDeFundo')
def index():
    imagens = ['1.jpg','2.jpg','3.jpg'];
    
    return send_file("imagens/" + imagens[randint(0,2)]);

app.run(host='0.0.0.0', port=8080,debug=True);
