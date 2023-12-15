#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
cant=int(input("Introduce la cantidad de notas: "))
for cont in range(cant):
    nota=float(input("Introduce tu nota: "))
    if nota>10 or nota<0:
        print("Nota equivocada")
    else:
        if  nota>=5:  
            print("Has aprobado")
        else:
            print("Has suspendido")