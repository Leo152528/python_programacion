#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random 
rand=random.randint(1,1000)
x="Incorrecto"
cont=0
while x=="Incorrecto":
    num=int(input("Introduce un valor entre 1 y 1000: "))
    while num>1000 or num<1:
        print("Número fuera del rango")
        num=int(input("Introduce otro valor entre 1 y 1000: "))
    if num==rand:
        x="Correcto"
        print(f"{x} y has usado {cont} intentos")
    else:
        if num<rand:
            x="Incorrecto"
            print("El número que has introducido es menor")
            cont=cont+1
        else:
            x="Incorrecto"
            print("El número que has introducido es mayor")
            cont=cont+1