#Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
cont=""
for var in range(0,100,3):
    if var==99:
        cont=cont+str(var)
    else:
        cont=cont+str(var)+","
print(cont)