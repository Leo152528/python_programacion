#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=int(input("Introduce un valor: "))
var2=int(input("Introduce otro valor: "))
if var1<var2:
    print("Var1 es menor qeu var2")
elif var1>var2:
    print("Var1 es mayor que var2")   
else:
    print("Var1 es igual que var2")
