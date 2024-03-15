#a,b,c,d,e,g
import random
nums=[]
cant=int(input("Introduce cuantas multiplicaciones quieres hacer: "))
val=input("Introduce el rango de las multiplicaciones con un espacio: ")
vals=val.split()
cant2=cant
while len(vals)==1:
    val=input("Introduce el otro rango de las multiplicaciones con un espacio: ")
    if val.isnumeric() or int(val)<0:
        vals.append(val)
        vals.sort()
        if int(vals[0])+int(vals[1])<0:
            vals.reverse()
puntos=0
res=0
while cant!=0 and res!="F":
    cant-=1
    num1=random.randint(int(vals[0]),int(vals[1]))
    num2=random.randint(int(vals[0]),int(vals[1]))
    result=num1*num2
    nums.append(result)
    res=input(f"{num1} x {num2}: ")
    if res.isnumeric():
        if int(res)==result:
            print("Correcto")
            puntos+=1
        else:
            res=input("Otro intento: ")
            if int(res)==result:
                print("Correcto")
                puntos+=0.5
            else:
                print("Incorrecto")
    else:
        print("Incorrecto")
print("Has acertado: ",puntos)
porc=(puntos*100)/cant2
puntosf=cant2-puntos
porce=(puntosf*100)/cant2
print(f"Has acertado un {porc:.0f} %")
print(f"Has acertado un {porce:.0f} %")
print("Las respuestas correctas eran:")
print(nums)
