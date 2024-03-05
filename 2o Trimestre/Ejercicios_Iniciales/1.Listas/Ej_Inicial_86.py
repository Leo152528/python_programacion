#Ejercicios DNIs
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
intentos=[]
ok=[]
nok=[]
intent=0
continuar=input("Quieres empezar s/n: ")
while continuar!="s" and continuar!="n":
    continuar=input("No le he entendido, que querias decir s/n: ")
while continuar=="s":
    dni=input("Introduce 8 dígitos de tu DNI:")
    if len(dni)!=8:
        print("Deben ser 8 dígitos")
        intentos.append("0")
        nok.append(dni)
    elif dni.isnumeric()==False:
        print("Debe ser numérico")
        intentos.append("1")
        nok.append(dni)
    else:
        num=int(dni)%23   
        if num>22 or num<0:
            print("DNI no existente")
            intentos.append("2")
            nok.append(dni)
        else:
            dni=dni+"-"+letras[num]
            intentos.append("3")
            ok.append(dni)
            print(dni)
    intent+=1
    continuar=input("Quieres introducir más DNIs s/n: ")
    while continuar!="s" and continuar!="n":
        continuar=input("No le he entendido, que querias decir s/n: ")
print("***Opciones***")
print("1.Lista de NIF correctos de menor a mayor")
print("2.Lista de DNI incorrectos de menor a mayor")
print("3.Cantidad de errores introducidos")
print("4.Cantidad de DNIs correctos")
print("5.Porcentages de intentos con error y sin error")
print("6.Salir s/n")
que=1
while que!=6:
    que=int(input("Escoge una opción: "))
    while que>6 and que<1:
        que=input("Escoge una opción entre 1 y 6: ")
    if que==1:
        print(ok)
    elif que==2:
        print(nok)
    elif que==3:
        print(len(nok))
    elif que==4:
        print(len(ok))
    elif que==5:
        print("Num. intentos es:",intent)
        print((len(ok)/intent)*100,"%")
        print((len(nok)/intent)*100,"%")
        print((intentos.count("0")/intent)*100,"%")
        print((intentos.count("1")/intent)*100,"%")
        print((intentos.count("2")/intent)*100,"%")