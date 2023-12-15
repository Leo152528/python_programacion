# Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
sum=0
cont=0
while sum<=50:
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
print("Programa finalizado")