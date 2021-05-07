#problema 1: ingrese un numero y halle su raiz cubica

#SOLUCION
import math
#variable de entrada
num = float(input("Ingrese un numero: "))
#variable de operacion
rc = math.pow(num, 1/3)
#variable de salida
print("La raiz cubica es: ",rc)