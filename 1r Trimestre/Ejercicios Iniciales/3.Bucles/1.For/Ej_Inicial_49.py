#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
password=str(input("Introduce una palabra secreta:"))
for cont in password:
    let=str(input("Introduce una letra: "))
    if let=="":
        print("El vacio no cuenta como letra")
    else:
        x=password.find(let)
        y=password.count(let)
        if x>-1:
            print("La letra existe, y está en la posicion ",x)
            if y>1:
                for cont in range(y-1):
                    z=password.rfind(let)
                    print("La letra existe, y está en la posicion ",z)
        else:
            print("La letra no existe")