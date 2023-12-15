#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra=str(input("Introduce una letra:"))
y=letra.isalpha()
if y==False:
    print("Ha introducido una letra no correspondiente")
else:
     x=letra.capitalize()
     if letra==x:
         print("Tu letra es mayúscula")
     else:
         print("Tu letra es minúscula")