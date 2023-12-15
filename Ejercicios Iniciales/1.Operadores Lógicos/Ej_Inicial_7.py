#Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
op1=int(input("Introduce un valor :"))
op2=int(input("Introduce otro valor :"))
suma=op1+op2
resta=op1-op2
mult=op1*op2
div=op1/op2
mod=op1%op2
expo=op1**op2
div_ent=op1//op2
print("La suma entre op1 y op2 es ",suma)
print("La resta entre op1 y op2 es ",resta)
print("La multiplicación entre op1 y op2 es ",mult)
print("La division entre op1 y op2 es ",f"{div:.2f}")
print("El módulo entre op1 y op2 es ",mod)
print("El exponente entre op1 y op2 es ",expo)
print("La division entera entre op1 y op2 es ",div_ent)
