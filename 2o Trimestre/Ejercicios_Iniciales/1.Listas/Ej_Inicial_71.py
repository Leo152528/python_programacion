#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
rep=input("Quieres empezar s/n: ")
while rep!="s" and rep!="n":
    rep=input("Perdone no le he entendido, s/n:")
lista=[]
while rep=="s":
    let=input("Introduce una letra:")
    while let.isalpha()==False:
        let=input("Introduce una letra:")
    if lista.count(let)<1:    
        lista.append(let)
    rep=input("Quieres repetir s/n: ")
    while rep!="s" and rep!="n":
        rep=input("No le he entendido, s/n:")
print(lista)