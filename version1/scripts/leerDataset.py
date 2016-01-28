#!/usr/bin/python
import hashlib
import sys


#inicializo la suma para los dataset pares e impares
sumaPares= 0;
sumaImpares=0;
for line in sys.stdin:
	#obtengo el numero de data set 
	arrayDataset = line.split(":")
	numeroDataset = arrayDataset[0];
	#limpio los espacios en blanco y eliminar el retorno de carro
	lineaNumeros = arrayDataset[1].strip();
	lineaNumeros = lineaNumeros.replace("\n","");
	#obtengo los numeros dentro de cada dataset
	arrayNumeros = lineaNumeros.split(" ")
	sumaInternaDataset = 0;
	if len(arrayNumeros)>0:
		for numero in arrayNumeros:
			sumaInternaDataset=sumaInternaDataset+int(numero);
	#compruebo si es impar o par el dataset

	if int(numeroDataset)%2==0:
		sumaPares = sumaPares + sumaInternaDataset	
	else:
		sumaImpares = sumaImpares + sumaInternaDataset	

print "La suma de los dataset pares es: "+unicode(sumaPares)+"\n"
print "La suma de los dataset impares es: "+unicode(sumaImpares)
