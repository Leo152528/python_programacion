#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random 
import time
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
fin=0
start=time.perf_counter()
while fin<3:
    x=random.randint(1,6)
    if x==1:
        n1+=1
    elif x==2:
        n2+=1
    elif x==3:
        n3+=1
    elif x==4:
        n4+=1
    elif x==5:
        n5+=1
    else:
        n6+=1
    fin=time.perf_counter()-start
print(fin)
print("Uno",n1)
print("Dos",n2)
print("Tres",n3)
print("Cuatro",n4)
print("Cinco",n5)
print("Seis",n6)