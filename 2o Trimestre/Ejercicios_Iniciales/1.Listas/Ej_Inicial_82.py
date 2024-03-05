#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
x=len(lista)
pal=random.randint(0,x-1)
adiv=""
while adiv!=lista[pal]:
    adiv=input("Introduce una palabra de la lista: ")
    if adiv==lista[pal]:
        print("Acertaste")
    else:
        print("Sigue jugando")