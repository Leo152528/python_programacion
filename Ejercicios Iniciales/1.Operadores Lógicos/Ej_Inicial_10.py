#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar
var1=float(input("Introduce un valor:"))
var2=float(input("Introduce otro valor:"))
coci=var1/var2
resto=var1%var2
print("El cociente de la division es: ",f"{coci:.2f}")
print("El resto de la división es :",resto)
if(var1%2==0):print("El dividendo es par")
else:print("el dividendo es impar")
