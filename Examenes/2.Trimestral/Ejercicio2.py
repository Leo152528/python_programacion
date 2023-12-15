varmin=int(input("Introduce el rango mínimo: "))
varmax=int(input("Introduce el rango máximo: "))
varint=int(input("Introduce el intervalo: "))
nums=""
for cont in range(varmin,varmax+1,varint):
    if cont==varmin:
        nums=nums+str(cont)
    else:
        nums=nums+","+str(cont)
print(nums)