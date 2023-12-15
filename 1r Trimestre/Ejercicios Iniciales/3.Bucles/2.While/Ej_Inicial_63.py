# Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
for cont in range(100):
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
print("Uno",n1)
print("Dos",n2)
print("Tres",n3)
print("Cuatro",n4)
print("Cinco",n5)
print("Seis",n6)