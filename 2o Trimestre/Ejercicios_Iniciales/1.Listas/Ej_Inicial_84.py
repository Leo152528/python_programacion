#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
x=len(lista)
pal=random.randint(0,x-1)
lista1=[]
for cont in lista[pal]:
    lista1.append(cont)
random.shuffle(lista1)
oport=3
adiv=""
while oport!=0 and adiv!=lista[pal]:
    print(lista1)
    adiv=input("Ordena esta palabra: ")
    oport-=1
    if adiv==lista[pal]:
        print("Acertaste")
    else:
        print("No has acertado")