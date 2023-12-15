#Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones:
#Debe tener una longitud entre 6 y 8 caracteres.
#Debe contener como mínimo:
#2 números mayores o iguales que 1 y menor o igual que 5
#2 letras minúsculas
#1 letra mayúscula
#2 símbolos (*, _, @, &,/,#)
#1 número mayor o igual que 6 y menor o igual que 5
password=input("Introduce tu contraseña: ")
long=len(password)
may1omen5=0
minu=0
mayu=0
simb=0
numeric=0
correcto="Password correcto"
incorrecto="Password incorrecto"
if long>10 or long<8:
    print("Password incorrecto")
else:
    for cont in range (long):
        if password[0+cont]=="1" or password[0+cont]=="2" or password[0+cont]=="3" or password[0+cont]=="4" or password[0+cont]=="5": 
            may1omen5+=1
        elif password[0+cont]=="*" or password[0+cont]=="_" or password[0+cont]=="@" or password[0+cont]=="&" or password[0+cont]=="/" or password[0+cont]=="#":
            simb=simb+1
        elif password[0+cont].isnumeric():
            numeric+=1
        elif password[0+cont].isalpha():
            if password[0+cont].isupper():
                    mayu+=1
            elif password[0+cont].islower():
                    minu+=1
    if may1omen5>=2:
        may1omen5=correcto
    else:
        may1omen5=incorrecto
    if minu>=2:   
        minu=correcto
    else:
        minu=incorrecto
    if mayu>=1:
        mayu=correcto
    else:
        mayu=incorrecto
    if simb>=2:
        simb=correcto
    else:
        simb=incorrecto
    if numeric>=1:
        numeric=correcto
    else:
        numeric=incorrecto
    if may1omen5==incorrecto or minu==incorrecto or mayu==incorrecto or simb==incorrecto or numeric==incorrecto:
        print("Password incorrecto")
    else:
        print("Password correcto")