#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
var1="A quién madruga Dios le ayuda"
print(var1)
palabra=str(input("Introduce una palabra de estas:"))
a=var1.find("A")
q=var1.find("quién")
m=var1.find("madruga")
d=var1.find("Dios")
l=var1.find("le")
ay=var1.find("ayuda")
if a<1 or q<1 or m<1 or d<1 or l<1 or ay<1:
    index=var1.index(palabra)
    print("Su palabra esta en la frase y tiene índice ",index)
else:
    print("Su palabra no esta en la frase")
