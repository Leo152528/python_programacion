#Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
x="s"
while x=="s":
    var1=int(input("Introduce un valor para sumar: "))
    var2=int(input("Introduce otro valor para sumar: "))
    total=var1+var2
    print("El resultado de la suma es: ",total)
    x=str(input("Deseas repetir la operación s/n:"))
print("Programa finalizado")