import random
apodo=input("Introduce tu apodo: ")
continuar="s"
while continuar=="s":
    apodo=0
    banca=0
    otra="s"
    while otra=="s" and apodo<7.5:
        cartaj=random.randint(1,12)
        while cartaj==8 or cartaj==9:
            cartaj=random.randint(1,12)
        print(f"Carta {apodo}: ",cartaj)
        if cartaj>=10:
            apodo=float(apodo)+0.5
        else:
            apodo=float(apodo)+float(cartaj)
        print(f"Suma de {apodo} : ",apodo)
        if apodo<=7.5:
            otra=input("Quieres otra carta s/n: ")
            while otra!="s" and otra!="n":
                otra=input("No le he entendido, que queria decir: ")
    while otra=="s" and banca<7.5:
        cartab=random.randint(1,12)
        while cartab==8 or cartab==9:
            cartab=random.randint(1,12)
        print("Carta de banca: ",cartab)
        if cartab>=10:
            apodo=float(apodo)+0.5
        else:
            apodo=float(apodo)+float(cartab)
        print("Suma banca: ",apodo)
        if apodo<=7.5:
            otra=input("Quieres otra carta s/n: ")
            while otra!="s" and otra!="n":
                otra=input("No le he entendido, que queria decir: ")
    