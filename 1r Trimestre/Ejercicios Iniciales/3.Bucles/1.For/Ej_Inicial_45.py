#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
pal=str(input("Intodice una palabra:"))
cons=""
voc=""
cant=0
for cont in pal:
    
    let=pal[0+cant]
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u" or let=="á" or let=="é" or let=="í" or let=="ó" or let=="ú":
        voc=voc+let
    else:
        cons=cons+let
    cant=cant+1
print(f"Las vocales de la palabra {pal} son: {voc}")
print(f"Las consonantes de la palabra {pal} son: {cons}")
