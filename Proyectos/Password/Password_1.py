#Crea una contrasenya
print("Istrucciones:")
print("Su contraseña debe ser entre 6 y 8 caracteres, incluyendolos")
print("Fuerza estos valores segun su posición")
print("    Posición 1: número entre 1 y 5, incluyendolos")
print("    Posición 2: letra minúscula")
print("    Posición 3: letra mayúscula")
print("    Posición 4: uno de estos símbolos: *,_,@")
print("    Posición 5: letra minúscula")
print("    Posición 6: número entre 6 y 9, incluyendolos")
print("    Posición 7: uno de estos símbolos:&,/,#")
print("    Posición 8: número menor o igual que 5")

password=input("Introduce una contraseña de 8 caracteres: ")
longitud=len(password)
error=""
if longitud<6 or longitud>8:
    print(f"“Error, el password té una longitud de {longitud} caràcters i no compleix els requisits")
else:
    x=int(password[0])
    y=password[1].casefold()
    z=password[2].capitalize()
    a=password[4].casefold()
    b=int(password[5])
    d=0
    
    if x>5 or x<1:
        error=(error+("*Error al caracter 1*"))
    car2=y.isalpha()
    if car2==False :
            error=(error+("*Error al caracter 2*"))
    else:
        if not y==password[1]:
            error=(error+("*Error al caracter 2*"))   
    car3=z.isalpha()
    if car3==False:
        error=(error+("*Error al caracter 3*"))
    else:
        if not z==password[2]:
            error=(error+("*Error al caracter 3*"))
    if password[3]=="*" or  password[3]=="_" or  password[3]=="@":
        d=d+1
    else:
        error=(error+("*Error al caracter 4*"))
    car5=a.isalpha()
    if a==False:
        error=(error+("*Error al caracter 5*"))
    else:
        if not a==password[4]:
            error=(error+("*Error al caracter 5*"))            
    if longitud==6:
        if b>9 or b<6:
            error=(error+("*Error al caracter 6*"))
        if error=="":
            print("Su contraseña es correcta")
        else:
            print(error)
    elif longitud==7: 
        if b>9 or b<6:
            error=(error+("*Error al caracter 6*"))
        if password[6]=="&" or  password[6]=="/" or  password[6]=="#":
           d=d+1 
        else:
            error=(error+("*Error al caracter 7*"))
        if error=="":
            print("Su contraseña es correcta")
        else:
            print(error)    
    else:
        c=int(password[7])
        if b>9 or b<6:
            error=(error+("*Error al caracter 6*"))
        if password[6]=="&" or  password[6]=="/" or  password[6]=="#":
            d=d+1
        else:
            error=(error+("*Error al caracter 7*"))
        if c>5:
            error=(error+("*Error al caracter 8*"))
        if error=="":
            print("Su contraseña es correcta")
        else:
            print(error)

#2Aa*a
#2Aa*a8#8a
#9aA*a8#3
#41A*a8#3
#4ba*a8#3
#4bA%a8#3
#4bA*T8#3
#4bA*t4#3
#4bA*t7*3
#4bA*t7#6
#8BA*t7#4
#8BA*t7#9
#1bB_a7/4
#1bB_a7/
#1bB_a7