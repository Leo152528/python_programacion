#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var1=int(input("Introduce la base mayor del trapecio: "))
var2=int(input("Introduce la base menor del trapecio: "))
var3=int(input("Introduce la altura del trapecio: "))
var4=int(input("Introduce los lados del trapecio: "))
per=var1+var2+var4+var4
print("El perímetro del trapecio es ",per)
ar=var3*((var1+var2)/2)
print("El área es ",ar)