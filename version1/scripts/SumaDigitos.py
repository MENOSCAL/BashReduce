#!/usr/bin/python

import hashlib
import sys

for line in sys.stdin:
	line1 = line.replace(":", "")
	line1 = line1.replace(" ", "")
	line1 = line1.replace("\n", "")
	#suma = ObtenerValor(line1)
	tmpSuma = 0 #variable contador
	for caracter in line1: #Por cada caracter en "LLave"
		tmpSuma += int(caracter) #Aumentamos el valor de tmpSuma en el valor ascii del caracter "actual"
	print tmpSuma
#print tmpSuma