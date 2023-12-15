#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
radio=float(input("Introduce el raio del círculo: "))
area=math.pi*(radio**2)
print("El área del círculo es ",f"{area:.2f}")
per=math.pi*2*radio
print("El perímetro del círculo es "f"{per:.2f}")