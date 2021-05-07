#Problema 2: hallar el volumen de un cilindro 

#SOLUCION
import math
#variable de entrada
r = float(input("Ingrese radio: "))
h = float(input("Ingrese altura: "))
#variable de operacion
vc = math.pi * math.pow(r, 2) * h
#variable de salida
print("Volumen del cilindro: ",vc)