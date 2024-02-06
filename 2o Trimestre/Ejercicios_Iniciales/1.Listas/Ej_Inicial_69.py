#Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
lista=[]
cant=int(input("Introduce cuantos numeros quieres introducir: "))
for cont in range(cant):
    valor=int(input("Introduce un número: "))
    lista.append(valor)
lista.sort()
print(lista)