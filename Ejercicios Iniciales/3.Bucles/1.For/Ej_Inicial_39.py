# Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
cant=int(input("Cantidad de num: "))
mayor0=0
menor0=0
igual0=0
for cont in range(cant):
    num=float(input("Introduce un numero: "))
    if num<0:
        menor0=menor0+1
    elif num>0:
        mayor0=mayor0+1
    else:
        igual0=igual0+1
print(f"Hay {menor0} numeros menor que 0")
print(f"Hay {mayor0} numeros mayor que 0")
print(f"Hay {igual0} numeros igual que 0")