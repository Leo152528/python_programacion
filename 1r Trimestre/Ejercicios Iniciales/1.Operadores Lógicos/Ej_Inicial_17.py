# Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=float(input("Introduce tu peso en kg:"))
altura=float(input("Introduce tu altura en m:"))
imc=peso/(altura**2)
print("Si pesas ",peso,"kilos y mides ",altura,", tu IMC es ",f"{imc:.2f}")
if imc>=25:
    print("Hay sobrepeso")