#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random 
rand=random.randint(1,5)
num=int(input("Introduce un valor entre 1 y 5: "))
while num>5 or num<1:
    print("Número fuera del rango")
    num=int(input("Introduce otro valor entre 1 y 5: "))
if num==rand:
    print("Número acertado")
else:
    print("Número no acertado")