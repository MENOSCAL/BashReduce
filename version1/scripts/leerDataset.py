#!/usr/bin/python
import hashlib
import sys


#inicializo la suma para los dataset pares e impares
sumaPares= 0;
sumaImpares=0;
for line in sys.stdin:
	#obtengo el numero de data set 
	numeroDataset = line.split(":")
	numeroDataset = numeroDataset[0];
	#limpio los espacios en blanco
	lineaNumeros = numeroDataset[1].strip();
	#obtengo los numeros dentro de cada dataset
	arrayNumeros = lineaNumeros.split(" ")
	sumaInternaDataset = 0;
	if len(arrayNumeros)>0:
		for numero in arrayNumeros:
			sumaInternaDataset=sumaInternaDataset+numero;
	#compruebo si es impar o par el dataset
	if numeroDataset%2==0:
		sumaPares = sumaPares + sumaInternaDataset	
	else:
		sumaImpares = sumaImpares + sumaInternaDataset	

print "La suma de los dataset pares es: "+sumaPares+"\n"
print "La suma de los dataset impares es: "+sumaImpares+"\n"
