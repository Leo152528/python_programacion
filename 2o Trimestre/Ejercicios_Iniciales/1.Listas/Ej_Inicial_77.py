#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
num=[]
let=[]
may=[]
ind=[]
min=[]
x=len(lista1)
for cont in range (x):
    if lista1[cont].isnumeric():
        num.append(lista1[cont])
    elif lista1[cont].isupper():
        may.append(lista1[cont])  
        min.append(lista1[cont].casefold())
    else:
        let.append(lista1[cont])
y=len(may)
let.extend(min)
aod=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente:"))
while aod!=1 and aod!=2:
    aod=int(input("No te he entendido 1 o 2:"))
num.sort()
let.sort()
for conta in range (y):
    ind.append(let.index(min[conta]))
    let.insert(ind[conta],may[conta])
    let.remove(min[conta])
if aod==1:
    print(num)
    print(let)
else:
    num.reverse()
    print(num)
    let.reverse()
    print(let)