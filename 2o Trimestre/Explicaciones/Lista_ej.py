con=input("Quieres introducir datos s/n:")
lista=[]
while con=="s":
    nomb=input("Introduce un nombre: ")
    alt=int(input("Introduce su altura: "))
    peso=int(input("Introduce su peso: "))
    edad=int(input("Introduce su edad: "))
    lista.append(nomb)
    lista.append(alt)
    lista.append(peso)
    lista.append(edad)
    con=input("Quieres introducir otra persona s/n: ")
rep=input("Quieres buscar datos s/n: ")
while rep=="s":
    pers=input("Introduce de quien quieres la información: ")
    x=lista.index(pers)
    if x>-1:
        print(lista[x+1:x+4])
    rep=input("Quieres buscar a otra persona s/n: ")