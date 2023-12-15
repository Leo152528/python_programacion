# Imprime el siguiente patrón utilizando for
cant=5
var1=54321
mult=10000
for cont in range(5):
    print(int(var1))
    var1=var1-(cant*mult)
    mult=mult/10
    cant=cant-1
    