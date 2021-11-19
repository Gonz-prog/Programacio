# Partiendo de 2 conjuntos:
# conjunto1 = {10, 20, 30, 40, 50}
# conjunto2 = {30, 40, 50, 60, 70}

conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}

# 1 Devolver un conjunto de los elementos idénticos 
# en los dos conjuntos.
uno3=[]
uno1=list(conjunto1)
uno2=list(conjunto2)
for i in uno2:
    if i in uno1:
        uno3.append(i)

uno4=set(uno3)

print("\n1:",uno4,"\n")

# 2 Vuelve un conjunto nuevo con todos los elementos 
# de los dos conjuntos eliminando los duplicados.

dos1=list(conjunto1)
dos2=list(conjunto2)

for i in dos2:
    if i not in dos1:
        dos1.append(i)

dos1.sort()
dos3=set(dos1)

print("2:",dos3,"\n")

# 3 Actualizar el primer conjunto con elementos 
# que sólo existen en el primer conjunto y no en el
# segundo conjunto.

c1=set(conjunto1)
c1.difference_update(conjunto2)

print("3:",c1,"\n")

# 4 Sacar los elementos 30, 40 del primer conjunto.

cuat1=list(conjunto1)

cuat1.pop(2)
cuat1.pop(3)

cuat2=set(cuat1)

print("4:",cuat2,"\n")

# 5 Devolver un conjunto de todos los elementos de 
# conjunt1 o conjunt2, pero no de ambos conjuntos.

cinc1=set(conjunto1)
cinc2=set(conjunto2)
cinc3=[]    
for i in range(len(cinc1)):
    x=cinc1.pop()
    y=cinc2.pop()
    cinc3.append(x)
    cinc3.append(y)
    

cinc4=set(cinc3)

print("5:",cinc4,"\n")
