#Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random 
rand=random.randint(1,5)
x=0
while x<3:
    num=int(input("Introduce un valor entre 1 y 5: "))
    while num>5 or num<1:
        print("Número fuera del rango")
        num=int(input("Introduce otro valor entre 1 y 5: "))
    if num==rand:
        print("Número acertado")
        x=x+3
    else:
        print("Número no acertado")
        x=x+1