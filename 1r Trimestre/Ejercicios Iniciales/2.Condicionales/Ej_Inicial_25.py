#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
var1=float(input("Introduce tu nota: "))
if var1<0 or var1>10:
    print("El valor esta fuera del rengo 0-10")
else:
    if var1<5:
       print("Tu nota es un insuficiente")
    elif var1<6.5 and var1>=5:
        print("Has aprobado con un suficiente")
    elif var1>=6.5 and var1<8.5:
        print("Has aprobado con un notable")
    else:
        print("Has aprobado con un excelente")