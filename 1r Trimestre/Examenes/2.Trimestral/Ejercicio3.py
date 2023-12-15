veces=int(input("Introduce una cantidad de digitos: "))
num=input("Introduce un digto: ")
x=len(num)
y=0
tot=0
if x==veces:
    for cont in range(veces):
        tot=tot+int(num[0+y])
        y=y+1
    print("Resultado:",tot)
else:
    print("Error, no coincide el número de cifras")
