#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuariotenga x oportunidades para ver si letra introducida está en esa palabra.
password=str(input("Introduce una palabra secreta: "))
for cont in password:
    let=str(input("Introduce una letra: "))
    x=password.find(let)
    if x>-1:
        print("La letra existe")
    else:
        print("La letra no existe")