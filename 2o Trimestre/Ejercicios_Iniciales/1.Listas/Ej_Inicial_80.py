# Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
lista=[]
lista.append(input("Introduce un valor para determinar si es decimal: "))
num=str(lista[0])
bien=num.split(".")
if len(bien)==2:
    if bien[0].isnumeric() and bien[1].isnumeric():
        if float(lista[0])-float(bien[0])>0:
            print("Es un decimal")
        else:
            print("No es un decimal")   
    else:
        print("No es un decimal")
else:
    print("No es un decimal")
