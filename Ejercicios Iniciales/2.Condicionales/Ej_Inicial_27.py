#Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
letra=str(input("Introduce una letra:"))
y=letra.isalnum()
if y==False:
   print("Tu letra no es ni número ni letra")
else:
    x=letra.isalpha()
    if x==False:
       print("Tu letra es un número")
    else:   
        z=letra.capitalize()
        if z==letra:
            print("Tu letra es mayúscula")
        else:
            print("Tu letra es minúscula")