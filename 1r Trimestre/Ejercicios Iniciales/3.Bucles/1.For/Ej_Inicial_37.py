#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
cant=int(input("Introduce la cantidad de notas: "))
for cont in range(cant):
    nota=float(input("Introduce tu nota: "))
    if nota>=5:
        print("Has aprobado")
    else:
        print("Has suspendido")