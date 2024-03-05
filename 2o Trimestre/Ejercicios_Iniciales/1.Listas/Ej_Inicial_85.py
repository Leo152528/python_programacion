#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
ing=[]
caste=[]
cata=[]
vez=0
continuar=input("Quieres empezar a introducir datos s/n: ")
while continuar!="s" and continuar!="n":
    continuar=input("No le he entendido, que querias decir s/n: ")
while continuar=="s":
    nom=input("Introduce un nombre: ")
    ingl=float(input("Introduce la nota de Inglés: "))
    while ingl>10 or ingl<0:
        ingl=float(input("Introduce la nota de Inglés del 1 al 10: "))
    ing.append(ingl)
    cast=float(input("Introduce la nota de Castellano: "))
    while cast>10 or cast<0:
        cast=float(input("Introduce la nota de Castellano del 1 al 10: "))
    caste.append(cast)
    cat=float(input("Introduce la nota de Catalán: "))
    while cat>10 or cat<0:
        cat=float(input("Introduce la nota de Catalán del 1 al 10: "))
    cata.append(cat)
    continuar=input("Quieres introducir más datos s/n: ")
    while continuar!="s" and continuar!="n":
        continuar=input("No le he entendido, que querias decir s/n: ")
    vez+=1
print("Notas de Inglés son: ",ing)
print("Notas de Castellano son: ",caste)
print("Notas de Catalán son: ",cata)
mediai=0
mediac=0
mediacata=0
sumi=0
sumc=0
sumcata=0
for cont in ing:
    sumi+=cont
    mediai=sumi/vez
print("La media de Inglés es: ",mediai)
for cont in caste:
    sumc+=cont
    mediac=sumc/vez
print("La media de Castellano es: ",mediac)
for cont in cata:
    sumcata+=cont
    mediacata=sumcata/vez
print("La media de Cataán es: ",mediacata)
ing.sort()
caste.sort()
cata.sort()
x=vez/2
if vez%2==0:
    x=int(x)  
    mi=(ing[x]+ing[x-1])/2
    mc=(caste[x]+caste[x-1])/2
    mcata=(cata[x]+cata[x-1])/2
else:
    x=x-0.5
    x=int(x)
    mi=ing[x]
    mc=caste[x]
    mcata=cata[x]
print("La mediana de Inglés es: ",mi)
print("La mediana de Castellano es: ",mc)
print("La mediana de Catalán es: ",mcata)