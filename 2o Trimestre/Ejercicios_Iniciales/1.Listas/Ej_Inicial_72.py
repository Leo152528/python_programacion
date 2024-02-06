#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
rep=input("Quieres empezar s/n: ")
while rep!="s" and rep!="n":
    rep=input("Perdone no le he entendido, s/n:")
lista=[]
while rep=="s":
    let=input("Introduce una letra:")
    while let.isalpha()==False:
        let=input("Introduce una letra:")
    if let=="á" or let=="à":
        let="a"
    if let=="é" or let=="è":
        let="e"
    if let=="í" or let=="ì":
        let="i"
    if let=="ó" or let=="ò":
        let="o"
    if let=="ú" or let=="ù":
        let="u"
    if lista.count(let)<1:    
        lista.append(let)
    rep=input("Quieres repetir s/n: ")
    while rep!="s" and rep!="n":
        rep=input("No le he entendido, s/n:")
print(lista)