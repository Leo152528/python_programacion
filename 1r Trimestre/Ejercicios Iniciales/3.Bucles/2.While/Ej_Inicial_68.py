#Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar introduciendo passwords. Ej. “¿Deseas introducir otro password s/n
continuar="s"
while continuar=="s":
    may1omen5=0
    minu=0
    mayu=0
    simb=0
    numeric=0
    correcto="Password correcto"
    incorrecto="Password incorrecto"
    password=input("Introduce tu contraseña: ")
    long=len(password)
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
    continuar=input("Introduce si quiere conituar s/n: ")