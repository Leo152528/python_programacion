#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
num=0
may=0
men=0
par=0
imp=0
pos=0
neg=0
cer=0
tot=0
while num!=(-99):
    num=int(input("Introduce un valor: "))
    if num>may:
        may=num
    elif num<men:
        men=num
    if num==-99:
        tot=tot+0
    else:
        x=num%2
        if x==0:
            par+=1
        else:
            imp+=1
        if num>0:
            pos+=1
        elif num==0:
            cer+=1
        else:
            neg+=1
        tot=tot+num
print("")
print("RESUMEN")
print("Número de pares es: ",par)
print("Número de impares es: ",imp)
print("Número de positivos es: ",pos)
print("Número de negativos es: ",neg)
print("El total es: ",tot)
print("El número más grande es ",may)
print("El número más pequeño es ",men)
