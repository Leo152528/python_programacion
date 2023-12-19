#Programa el código que gestione una partida. El programa ofrece una carta, el usuario puede o no
#aceptar. La puntuación se acumula según el número de carta que aparece al azar. Si consigues que:
#La puntuación de 7.5, el programa te felicita. "Enhorabuena, has ganado la partida"
#Si te pasas de 7.5, el programa informa: "Has perdido la partida!"
#Si te plantas con una puntuación entre 6 y 7 "Has sido un poco conservador"
#Si te plantas con una puntuación inferior a 6. "Quizás tendrías que arriesgar un poco ¿no?
#El programa te debe dar la opción de repetir o no una nueva partida.
import random
continuar="s"
while continuar=="s":
    total=0
    otra="s"
    while otra=="s" or total<7.5:
        carta=random.randint(1,12)
        while carta==8 or carta==9:
            carta=random.randint(1,12)
        print("Tu carta es: ",carta)
        if carta>=10:
            total=total+0,5
        else:
            total=total+carta
        print("Tu suma es de: ",total)
        otra=input("Quieres otra carta s/n: ")
    if total==7.5:
        print("Enhorabuena, has ganado la partida")
    elif total>7.5:
        print("¡Has perdido la partida!")
    elif total>=6 and total<=7:
        print("Has sido un poco conservador")
    else:
        print("Quizás tendrías que arriesgar un poco ¿no?")
    continuar=input("Introduce si quieres otra parida s/n:")
