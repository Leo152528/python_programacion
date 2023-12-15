#. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
x="s"
sum=0
cont=0
while x=="s":
    var1=int(input("Introduce un valor para sumar: "))
    var2=int(input("Introduce otro valor para sumar: "))
    total=var1+var2
    sum=sum+total
    cont=cont+1
    print("El resultado de la suma es: ",total)
    x=str(input("Deseas repetir la operación s/n:"))
print("Resumen:")
print(f"la suma total es: {sum} y el número de repeticiones es: {cont}")
print("Programa finalizado")