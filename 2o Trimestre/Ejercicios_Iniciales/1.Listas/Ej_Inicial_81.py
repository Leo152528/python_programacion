#A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
x=len(lista)
pal=random.randint(0,x-1)
print(lista[pal])