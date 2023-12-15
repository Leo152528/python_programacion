#Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
sum=0
cont=0
y=0
while sum>=50 or y==0:
    var1=int(input("Introduce un valor para sumar: "))
    var2=int(input("Introduce otro valor para sumar: "))
    total=var1+var2
    sum=sum+total
    cont=cont+1
    print("El resultado de la suma es: ",total)
    if cont==1:
        print(f"El total acomulado es: {sum} y llevas {cont} operación realizada")
    else:
        print(f"El total acomulado es: {sum} y llevas {cont} operaciónes realizadas")
    y=sum%2
print("Programa finalizado")