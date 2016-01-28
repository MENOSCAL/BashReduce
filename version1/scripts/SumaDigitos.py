#!/usr/bin/python

import hashlib
import sys

m = hashlib.md5()

for line in sys.stdin:
	line.replace(" ", "")
	line.replace(":", "")
	suma = ObtenerValor(line)

	print suma

def ObtenerValor(line):
	tmpSuma = 0 #variable contador
	for caracter in line: #Por cada caracter en "LLave" 
		tmpSuma += ord(caracter) #Aumentamos el valor de tmpSuma en el valor ascii del caracter "actual"
	return tmpSuma

        