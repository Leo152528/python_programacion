#Crea un programa que cuente todos los números pares hasta el número 50
par=0
impar=0
for cont in range(0,50):
    var=cont%2
    if var==0:
        par=par+1
    else:
        impar=impar+1
print(f"Hay {par} numeros pares")
print(f"Hay {impar} numeros impares")