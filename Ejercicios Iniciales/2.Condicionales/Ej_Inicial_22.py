#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
var1=float(input("Introduce tu nota: "))
if var1<0 or var1>10:
    print("El valor esta fuera del rengo 0-10")
else:
    if var1<5:
       print("Tu nota esta suspendida")
    else:
         print("Tu nota esta aprobada")   
   