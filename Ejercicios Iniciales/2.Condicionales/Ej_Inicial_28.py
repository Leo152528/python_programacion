#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=str(input("Introduce una letra:"))
y=letra.isalnum()
x=letra.isalpha()
z=letra.capitalize()
if y==False:
   print("Has introducido un símbolo")
elif x==False:
    print("Has introducio un número")
else:      
    if z==letra:
        print("Tu letra es mayúscula")
    else:
        print("Tu letra es minúscula")