#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio=float(input("Introduce el radio del cilindro: "))
altura=float(input("Introduce la altura del cilindro"))
area=math.pi*2*radio*(altura+radio)
vol=math.pi*altura*(radio**2)
print("El área del cilindro es ",f"{area:.2f}",", el volumen es ",f"{vol:.2f}")