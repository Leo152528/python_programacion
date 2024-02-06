#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
lista=[]
cant=int(input("Introduce la cantiadad de palabras: "))
for cont in range(cant):
    pal=input("Introduce una palabra: ")
    lista.append(pal)
lista.sort()
lista2=lista.copy()
lista2.reverse()
print(f"Lista1 contiene:{lista}")
print(f"lista2 contiene:{lista2}") 