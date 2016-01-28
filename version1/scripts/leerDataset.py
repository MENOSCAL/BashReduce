#!/usr/bin/python
import hashlib
import sys


m = hashlib.md5()
#inicializo la suma para los dataset pares e impares
suma= 0;
for line in sys.stdin:
	#obtengo el numero de data set 
	line1 = line.strip();
	line1 = line1.replace(" ","");
	line1 = line1.replace(":","");
	line1 = line1[0:10];
	line1 = int(line1);
	suma = line1;
	m.update(str(suma))
	print m.hexdigest()
print "La suma de los dataset es: "+unicode(suma)
m.update(str(suma))
print "Su hexadecimal es: "+unicode(m.hexdigest())
