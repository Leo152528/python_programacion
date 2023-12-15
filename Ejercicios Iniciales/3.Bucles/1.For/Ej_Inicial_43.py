# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
pal=str(input("Introduce una palabra: "))
cont=0
for var in pal:
    print(f"En posición {cont} la letra es {var} ")
    cont=cont+1