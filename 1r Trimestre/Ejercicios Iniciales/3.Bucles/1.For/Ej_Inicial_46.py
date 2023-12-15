#A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
pal=str(input("Intodroce una palabra:"))
cons=""
voc=""
cant=0
x=pal.casefold()
for cont in pal:
    
    let=x[0+cant]
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u" or let=="á" or let=="é" or let=="í" or let=="ó" or let=="ú":
        voc=voc+let
    else:
        cons=cons+let
    cant=cant+1
print(f"Las vocales de la palabra {pal} son: {voc}")
print(f"Las consonantes de la palabra {pal} son: {cons}")