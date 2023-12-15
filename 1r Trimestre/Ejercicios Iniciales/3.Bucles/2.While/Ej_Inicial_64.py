#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
par=0
imp=0
pos=0
neg=0
cer=0
num=0
tot=0
while num!=(-99):
    num=int(input("Introduce un valor: "))
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