#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
long=len(lista1)
numeric=0
mayus=0
let=0
sum=0
print(f"Num valores:{long}")
for cont in range(long):
    if lista1[cont].isnumeric()==True:
        numeric+=1
        sum+=int(lista1[cont])
    elif lista1[cont].isupper()==True:
        mayus+=1
        let+=1
    else:
        let+=1
print(f"Cantidad de números: {numeric}")
print(f"Cantidad de letras: {let}")
print(f"Cantidad de mayúsculas: {mayus}")
print(f"Suma total: {sum}")