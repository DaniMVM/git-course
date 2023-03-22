from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
	return "Daniela V.C"

@app.route('/hello')
def greating():
	return "HELLO WORLD"

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int, b:int):
	sum = a+b
	return  f"la suma es: {str(sum)}"