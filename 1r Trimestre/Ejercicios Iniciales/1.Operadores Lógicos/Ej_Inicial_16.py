#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
var1=float(input("Introduce un radicando: "))
raiz=math.sqrt(var1) 
print("La raíz del radicando es ",raiz)
raizentredos=int(raiz/2)
print("La raíz entre 2 es ",f"{raizentredos:.1f}")
