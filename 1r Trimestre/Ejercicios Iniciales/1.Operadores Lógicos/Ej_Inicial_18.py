#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
mayores=int(input("Introduce la cantidad de personas mayores de 18 hay:"))
menores=int(input("Introduce la cantidad de personas menores de 18 hay:"))
preciomayores=mayores*12*0.9
preciomenores=menores*12*0.5
print("El precio total del cine para ",menores," menor/es es: ",preciomenores)
print("El precio total del cine para ",mayores," adulto/s es: ",preciomayores)