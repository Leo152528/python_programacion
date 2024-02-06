# Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
lrep=[]
lnrep=[]
for cont in range (0,6):
    rep=lista1.index(lista2[cont])
    if rep>-1:
        lrep.append(lista1[rep])
    else:
        lnrep.append(lista1[rep])
print(lrep)
print(lnrep)