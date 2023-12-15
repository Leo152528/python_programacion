#Ejercicio 4
print("**********GASOLINERA**********")
print("Introduzca 1 para: Sin Plomo 95")
print("Introduzca 2 para: Sin Plomo 98")
print("Introduzca 3 para: Gasóleo A")
print("Introduzca 4 para: Gasóleo A+")
print("********************************")
tipo=int(input("Introduzca el tipo de combustible: "))
litros=int(input("Introduzca los litros de combustible: "))
if tipo<1 or tipo>4:
    print("No existe ese combustible")
else:
    if tipo==1:
        precio=1.765*litros
        print(f"Tu total a pagar es {precio}")
    elif tipo==2:
        precio=1.913*litros
        descuento=precio*0.9
        print(f"Tu total a pagar es {precio}, y con el descuento se queda en {descuento:.2f}")
    elif tipo==3:
        precio=1.746*litros
        print("Tu total a pagar es ",precio)
    else:
        precio=1.839*litros
        descuento=precio*0.88
        print(f"Tu total a pagar es {precio}, y con el descuento se queda en {descuento:.2f}")