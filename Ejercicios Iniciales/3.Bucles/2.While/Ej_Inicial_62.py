#Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
x=int(input("Introduce un valor: "))
y=int(input("Introduce un valor: "))
par=""
imp=""
if x<y:
    a=y%2
    if a==0:
        for cont in range(x,y+1):
            z=cont%2
            if z==0:
                if cont==y:
                    par=par+str(cont)
                else:
                    par=par+str(cont)+","
            else: 
                if cont==y-1:
                    imp=imp+str(cont)
                else:
                    imp=imp+str(cont)+","
    else:
        for cont in range(x,y+1):
            z=cont%2
            if z==0:
                if cont==y-1:
                    par=par+str(cont)
                else:
                    par=par+str(cont)+","
            else: 
                if cont==y:
                    imp=imp+str(cont)
                else:
                    imp=imp+str(cont)+","
    print(f"Los pares son: {par}")
    print(f"Los impares son: {imp}")
else:
    a=x%2
    if a==0:
        for cont in range(y,x+1):
            z=cont%2
            if z==0:
                if cont==x:
                    par=par+str(cont)
                else:
                    par=par+str(cont)+","
            else: 
                if cont==x-1:
                    imp=imp+str(cont)
                else:
                    imp=imp+str(cont)+","
    else:
        for cont in range(y,x+1):
            z=cont%2
            if z==0:
                if cont==x-1:
                    par=par+str(cont)
                else:
                    par=par+str(cont)+","
            else: 
                if cont==x:
                    imp=imp+str(cont)
                else:
                    imp=imp+str(cont)+","
    print(f"Los pares son: {par}")
    print(f"Los impares son: {imp}")