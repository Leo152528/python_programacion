pos=0
neg=0
for cont in range(5):
    num=int(input("Introduce un valor: "))
    if num>=0:
        pos=pos+num
    else:
        neg=neg+num
print(f"La suma de los valores positivos son:{pos}")
print(f"La suma de los valores pegativos son:{neg}")