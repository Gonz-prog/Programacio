# •Actualizar conjunto1 añadiendo elementos del conjunto2, 
# excepto los elementos que son iguales.

conjunto1 = {10, 20, 30, 40, 50} 
conjunto2 = {30, 40, 50, 60, 70}

s1=list(conjunto1)
s2=list(conjunto2)

lista=[]

for i in s2:
    if i not in s1:
        lista.append(i)
s1.append(lista)



print("\nConjunto actualizado",s1,"\n")

# •Eliminar elementos de conjunto1 que no estén en el 
# 1ºy el 2ºconjunto.
