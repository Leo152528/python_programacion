import random
ppt=input("Introduce si quieres sacar piedra, papel o tijera: ")
while ppt!="papel" and ppt!="tijera" and ppt!="piedra":
    ppt=input("Error, introduce si quieres sacar piedra, papel o tijeras: ")
ppto=random.randint(1,3)
if ppto==1:
    ppto="tijera"
elif ppto==2:
    ppto="piedra"
else:
    ppto="papel"
print(f"El ORDENADOR ha sacado:{ppto} y el USUARIO ha sacado:{ppt}")
if ppt=="tijera":
    if ppto=="tijera":
        print("Empate")
    elif ppto=="piedra":
        print("Gana ordenador")
    elif ppto=="papel":
        print("Gana usuario")
elif ppt=="papel":
    if ppto=="tijera":
        print("Gana ordenador")
    elif ppto=="piedra":
        print("Gana usuario")
    elif ppto=="papel":
        print("Empate")
elif ppt=="piedra":
    if ppto=="tijera":
        print("Gana usuario")
    elif ppto=="piedra":
        print("Empate")
    elif ppto=="papel":
        print("Gana ordenador")