#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
lrep=[]
lnrep=[]
for cont in range (5):
    for conta in range (6):
        if lista1[cont]==lista2[conta]:
            lrep.append(lista2[conta])
        else:
            if lista1.count(lista2[conta])==0 and lista2.count(lista1[cont])==0:
                if lnrep.count(lista2[conta])<1 and lnrep.count(lista1[cont])<1:
                    lnrep.append(lista2[conta])
                    lnrep.append(lista1[cont])
print("Estan repetidas:",lrep)
print("No estan repetidas:",lnrep)    