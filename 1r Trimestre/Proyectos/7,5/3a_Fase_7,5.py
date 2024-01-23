import random
apodo=input("Introduce tu apodo: ")
continuar=input(f"Quieres empezar una partida {apodo} s/n: ")
while continuar!="s" and continuar!="n":
    continuar=input("No le he entendido, que queria decir: ")
while continuar=="s":
    sapodo=0
    banca=0
    otraa="s"
    otrab="s"
    while otraa=="s" and sapodo<7.5:
        cartaj=random.randint(1,12)
        while cartaj==8 or cartaj==9:
            cartaj=random.randint(1,12)
        print(f"Carta {apodo}: ",cartaj)
        if cartaj>=10:
            sapodo=float(sapodo)+0.5
        else:
            sapodo=float(sapodo)+float(cartaj)
        print(f"Suma de {apodo} : ",sapodo)
        if sapodo<=7.5:
            otraa=input("Quieres otra carta s/n: ")
            while otraa!="s" and otraa!="n":
                otraa=input("No le he entendido, que queria decir: ")
    print("*****Turno de Bnca******")
    while otrab=="s":
        cartab=random.randint(1,12)
        while cartab==8 or cartab==9:
            cartab=random.randint(1,12)
        print("Carta de banca: ",cartab)
        if cartab>=10:
            banca=float(banca)+0.5
        else:
            banca=float(banca)+float(cartab)
        print("Suma banca: ",banca)
        if banca<7:
            otrab="s"
        else:
            otrab="n"
    if banca>5 and banca<7.5:
        if sapodo<banca:
            print("Banca ha ganado")
        elif sapodo==banca:
            print("Ha habido un empate")
        elif sapodo>7.5:
            print("Banca ha ganado")
        elif sapodo>banca:
            print(apodo," ha ganado")
    elif sapodo==7.5:
        if banca<sapodo:
            print(apodo," ha ganado")
        elif banca==sapodo:
            print("Ha habido un empate")
    elif banca>7.5:
        if sapodo>7.5:
            print(f"Banca y {apodo} han perdido")
        elif sapodo<7.5:
            print(apodo," ha ganado")
    continuar=input("Desea hacer otra partida s/n:")
    while continuar!="s" and continuar!="n":
                continuar=input("No le he entendido, que queria decir: ")