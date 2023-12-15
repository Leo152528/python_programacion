#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar essuperior o igual a 40
num=int(input("Introduce un valor para saber la tabla der multiplicar: "))
x=1
y=0
z=0
while not y>=40 and y!=num*10:
    y=num*x
    print(y)
    x+=1
    if y<=40:
        z+1
    else:
        print("Fin del programa")
