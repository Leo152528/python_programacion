import random
puntos=100
while puntos>0 :
    total=0
    otra="s"
    while otra=="s":
        carta=random.randint(1,12)
        while carta==8 or carta==9:
            carta=random.randint(1,12)
        print("Tu carta es: ",carta)
        if carta>=10:
            total=float(total)+0.5
        else:
            total=float(total)+float(carta)
        print("Tu suma es de: ",total)
        otra=input("Quieres otra carta s/n: ")
    if total==7.5:
        print("Enhorabuena, has ganado la partida")
        puntos+=10
    elif total>7.5:
        puntos-=10
        print("¡Has perdido la partida!")
    elif total>=6 and total<=7:
        print("Has sido un poco conservador")
        puntos+=5
    else:
        print("Quizás tendrías que arriesgar un poco ¿no?")
        puntos-=5
    continuar=input("Introduce si quieres otra parida s/n:")