#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
val1=int(input("Iniroduce un valor de intervalo: "))
val2=int(input("Iniroduce otro valor de intervalo: "))
nums=""
pos=0
z=val1
if val1<val2:
    for cont in range (val1,val2+1):
        if cont==val2:
            nums=nums+str(cont)
        else:
            nums=nums+str(cont)+"-"
    print(nums)
else:
    for x in range(val2-1,val1):
        pos=pos+1
        if pos==val2:
            nums=nums+str(z)
            z=z-1
        else: 
            nums=nums+str(z)+"-"
            z=z-1
    print(nums)