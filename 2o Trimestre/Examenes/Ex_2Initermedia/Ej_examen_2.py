import random
conc=""
cont=input("Quieres empezar una partida s/n: ")
while cont!="s" and cont!="n":
    cont=input("Error, quieres empezar una partida s/n: ")
while cont=="s":
    ppt=input("Introduce si quieres sacar piedra, papel o tijera: ")
    x=ppt.casefold()
    while x!="papel" and x!="tijera" and x!="piedra":
        ppt=input("Error, introduce si quieres sacar piedra, papel o tijeras: ")
        x=ppt.casefold()
    ppto=random.randint(1,3)
    if ppto==1:
        ppto="tijera"
    elif ppto==2:
        ppto="piedra"
    else:
        ppto="papel"
    print(f"El ORDENADOR ha sacado:{ppto} y el USUARIO ha sacado:{x}")
    if x=="tijera":
        if ppto=="tijera":
            print("Empate")
            conc=conc+"E"
        elif ppto=="piedra":
            print("Gana ordenador")
            conc=conc+"O"
        elif ppto=="papel":
            print("Gana usuario")
            conc=conc+"U"
    elif x=="papel":
        if ppto=="tijera":
            print("Gana ordenador")
            conc=conc+"O"
        elif ppto=="piedra":
            print("Gana usuario")
            conc=conc+"U"
        elif ppto=="papel":
            print("Empate")
            conc=conc+"E"
    elif x=="piedra":
        if ppto=="tijera":
            print("Gana usuario")
            conc=conc+"U"
        elif ppto=="piedra":
            print("Empate")
            conc=conc+"E"
        elif ppto=="papel":
            print("Gana ordenador")
            conc=conc+"O"
    print(f"Resultados:{conc}")
    cont=input("Quieres repetir una partida s/n: ")
    while cont!="s" and cont!="n":
        cont=input("Error, quieres repetir una partida s/n: ")
