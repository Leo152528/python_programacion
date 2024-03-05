# A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
con=input("Quieres empezar s/n: ")
while con!="s" and con!="n":
    con=input("No te he entendido s/n: ")
while con=="s":
    lista=["a","b","D","x","r","X","3","h","w","2","i"]
    elim=input("Introduce un valor que quieras eliminar: ")
    if elim.isalpha():
        print("Inroduce un valor")
    else:
        if lista.count(elim)>0:
            lista.remove(elim)
            print(lista)
        else:
            print("Valor introducido no esta en la lista")
    con=input("Deseas introducir otro valor s/n: ")
    while con!="s" and con!="n":
        con=input("No te he entendido s/n")