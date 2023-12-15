var_total=50
num=1
while var_total<=60 and num!=0:
    num=int(input("Introduce un valor: "))
    x=num%2
    if x==0:
        var_total=var_total+num
    else:
        var_total=var_total-num
    if var_total<=60:
        print(var_total)
    else:
        print("Fin del programa")
