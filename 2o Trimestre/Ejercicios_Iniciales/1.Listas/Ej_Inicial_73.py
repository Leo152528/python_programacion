# Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
lrep=[]
lnrep=[]
for cont in range (5):
    for conta in range (6):
        if lista1[cont]==lista2[conta]:
            lrep.append(lista2[conta])
        else:
            if lista1.count(lista2[conta])==0:
                if lnrep.count(lista2[conta])<1:
                    lnrep.append(lista2[conta])
print("Estan repetidas:",lrep)
print("No estan repetidas:",lnrep)    