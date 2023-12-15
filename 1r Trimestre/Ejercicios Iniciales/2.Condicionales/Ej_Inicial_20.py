#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("Introduce un valor: "))
var2=int(input("Introduce otro valor: "))
if var1<0 or var1>10 or var2<0 or var2>10:
    print("Algun valor esta fuera del rengo 0-10")
else:
    if var1<var2:
       print("Var1 es menor qeu var2")
    elif var1>var2:
         print("Var1 es mayor que var2")   
    else:
        print("Var1 es igual que var2")