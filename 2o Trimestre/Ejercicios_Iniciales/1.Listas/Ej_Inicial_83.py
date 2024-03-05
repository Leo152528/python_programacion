#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
x=len(lista)
puntuacion=0
puntuaciones=[]
partidas=0
continuar=input("Quieres empezar una partida s/n: ")
while continuar!="s" and continuar!="n":
    continuar=input("No le he entendido, que querias decir: ")
while continuar=="s":
    puntos=8
    partidas+=1
    adiv=""
    pal=random.randint(0,x-1)
    while adiv!=lista[pal]:
        adiv=input("Introduce una palabra de la lista: ")
        if adiv==lista[pal]:
            print("Acertaste")
            puntuacion+=puntos
            puntuaciones.append(puntos)
        else:
            print("Sigue jugando")
            puntos-=1
    continuar=input("Quieres empezar otra partida s/n: ")
    while continuar!="s" and continuar!="n":
        continuar=input("No le he entendido, que querias decir s/n: ")
if partidas>0:    
    print("Puntuacion: ",puntuaciones)
    print("Tu puntuación ha sido: ",puntuacion)
    print("La media ha sido de: ",partidas*4)
    if partidas*4<puntuacion:
        print("Tienes buena suerte")
    else:
        print("Dedicate a otra cosa")

