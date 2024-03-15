import random
nums=[]
puntos=0
for cont in range(10):
    num1=random.randint(0,10)
    num2=random.randint(0,10)
    result=num1*num2
    nums.append(result)
    res=input(f"{num1} x {num2}: ")
    if res.isnumeric():
        if res==result:
            print("Correcto")
            puntos+=1
        else:
            print("Incorrecto")
    else:
        print("Incorrecto")
print("Has hacertado: ",puntos)
print("Las respuestas correctas eran:")
print(nums)
