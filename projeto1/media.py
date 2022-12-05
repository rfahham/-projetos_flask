from flask import Flask
app = Flask(__name__)

@app.route("/")

def media():
	valor1 = raw_input("Digite o primeiro valor: ")
	valor2 = raw_input("Digite o segundo valor: ")
	valor3 = raw_input("Digite o terceiro valor: ")
	soma = valor1 + valor2 + valor3
	#media = soma / 3

	return soma
	
