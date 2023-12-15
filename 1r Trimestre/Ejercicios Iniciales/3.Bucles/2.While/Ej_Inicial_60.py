#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
num=int(input("Introduce un valor para saber la tabla der multiplicar: "))
x=1
y=0
while not y==num*10:
    y=num*x
    print(y)
    x+=1