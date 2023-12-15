#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
var1=float(input("Introduce tu nota: "))
if var1<0 :
    print("El valor esta fuera del rengo 0-10")
elif var1>10:
     print("El valor esta fuera del rengo 0-10")
else:
    if var1<5:
       print("Tu nota es un insuficiente")
    else:
        if var1<6.5:
            print("Has aprobado con un suficiente")
        else:
            if var1<8.5:
                print("Has aprobado con un notable")
            else:
                print("Has aprobado con un excelente")