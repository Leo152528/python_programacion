#Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. 
print("MENÚ:")
print("1.Bocadillo de calamares - 9€")
print("2.Bocadillo de chistorra - 4.5€")
print("3.Bikini de jamón - 2.5€")
print("")
print("ACOMPAÑAMIENTO:")
print("1.Patatas finas - 1.5€")
print("2.Patatas gruesas - 1.75€")
print("3.Patatas rústicas - 2€")
print("")
print("BEBIDAS:")
print("1.Coca Cola - 2€")
print("2.Acuarius - 1.5€")
print("3.Agua - 1€")
print("")
x="si"
dinero=0
ped=0
while x=="si":
    menu=int(input("Introduce el número del menú que quieras: "))
    acomp=int(input("Introduce el número del acompañante que quieras: "))
    beb=int(input("Introduce el número de la bebida que quieras: "))
    while menu>3 or menu<0:
        print("Ese menú no existe, introduzca otro valor que este en el menú")
        menu=int(input("Introduce el número del menú que quieras: "))
    while acomp>3 or acomp<0:
        print("Ese acompañante no existe, introduzca otro valor que este en el menú")
        acomp=int(input("Introduce el número del acompañante que quieras: "))
    while beb>3 or beb<0:
        print("Esa bebida no existe, introduzca otro valor que este en el menú")
        beb=int(input("Introduce el número de la bebida que quieras: "))
    if menu==1:
        dinero=dinero+9
    elif menu==2:
        dinero=dinero+4.5
    else:
        dinero=dinero+2.5
    if acomp==1:
        dinero=dinero+1.5
    elif acomp==2:
        dinero=dinero+1.75
    else:
        dinero=dinero+2
    if beb==1:
        dinero=dinero+2 
    elif beb==2:
        dinero=dinero+1.5
    else:
        dinero=dinero+1
    ped=ped+1
    x=str(input("Desea hacer otro pedido si sí,introduzca *si*,si no, introduzca *no*: "))
iva=dinero+(dinero*0.1)
if iva>30:
    desc=iva*0.85
elif iva>20 and iva<30:
    desc=iva*0.95
else:
    desc=iva
if ped>1:
    print("Han habido ",ped," pedidos.")
else:
    print("Ha habido ",ped," pedido")
print("Total a pagar: ",dinero)
print(f"Tontal con IVA: {iva:.2f}")
print(f"Total con descuento: {desc:.2f}")
