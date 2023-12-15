#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
var1="a quién madruga dios le ayuda"
print("A quién madruga dios le ayuda")
palabra=str(input("Introduce una palabra de estas:"))
x=palabra.casefold()
a=var1.find("a")
q=var1.find("quién")
m=var1.find("madruga")
d=var1.find("dios")
l=var1.find("le")
ay=var1.find("ayuda")
if a<1 or q<1 or m<1 or d<1 or l<1 or ay<1:
    index=var1.index(x)
    print("Su palabra esta en la frase y tiene índice ",index)
else:
    print("Su palabra no esta en la frase")
