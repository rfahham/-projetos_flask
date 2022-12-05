#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")

def media():

	dias = int(input('Quantos dias alugados? '))
	km = float(input('Quantos kms rodados? '))
	valor = float(input('Valor do KM rodado? '))
	pago = (dias * valor) + (km + 0.15)
	
	return ('O total a pagar é de R$ {}'.format(pago))