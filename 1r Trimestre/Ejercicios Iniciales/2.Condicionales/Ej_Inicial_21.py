#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
x2=float(input("Intoduce el valor de la x2:"))
x=float(input("Intoduce el valor de la x:"))
num=float(input("Intoduce el valor del valor solitario:"))
lodelaraiz=x*x-4*x2*num
if lodelaraiz<0:
    print("Lo de dentro de la raiz es negativo y no se puede calcular")
else:
    raiz=math.sqrt(lodelaraiz)
    totalarribapositivo_x= (-x+raiz)/(2*x2)
    totalarribapositivo_x2= totalarribapositivo_x**2
    totalarribanegativo_x= (-x-raiz)/(x**2)
    totalarribanegativo_x2= totalarribanegativo_x**2
    print("x=",totalarribapositivo_x,"y x2=",totalarribapositivo_x2," en caso de que se sume,en caso de que se reste x=", totalarribanegativo_x," y x2=", totalarribanegativo_x2)