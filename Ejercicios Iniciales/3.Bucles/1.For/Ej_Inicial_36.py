#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
cant=int(input("Introduce un valor: "))
num=0
val=0
for cont in range(cant):
    num=num+val+1
    val=val+1
print(f"La suma total de los num. naturales es: {num}")