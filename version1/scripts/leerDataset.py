#!/usr/bin/python
import hashlib
import sys


#inicializo la suma para los dataset pares e impares
sumaPares= 0;
sumaImpares=0;
for line in sys.stdin:
	#obtengo el numero de data set 
	arrayDataset = line.split(":")
	print arrayDataset
	numeroDataset = arrayDataset[0];
	#limpio los espacios en blanco y eliminar el retorno de carro
	lineaNumeros = arrayDataset[1].strip();
	lineaNumeros = lineaNumeros.replace("\n","");
	print lineaNumeros
	#obtengo los numeros dentro de cada dataset
	arrayNumeros = lineaNumeros.split(" ")
	print arrayNumeros
	sumaInternaDataset = 0;
	if len(arrayNumeros)>0:
		for numero in arrayNumeros:
			print numero
			sumaInternaDataset=sumaInternaDataset+int(numero);
			print sumaInternaDataset
	#compruebo si es impar o par el dataset
	if int(numeroDataset)%2==0:
		sumaPares = sumaPares + sumaInternaDataset	
	else:
		sumaImpares = sumaImpares + sumaInternaDataset	

print "La suma de los dataset pares es: "+sumaPares+"\n"
print "La suma de los dataset impares es: "+sumaImpares+"\n"
