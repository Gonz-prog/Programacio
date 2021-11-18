# Partiendo de 2 conjuntos:
# conjunto1 = {10, 20, 30, 40, 50}
# conjunto2 = {30, 40, 50, 60, 70}

# •1: Devolver un conjunto de los elementos idénticos 
# en los dos conjuntos.

# •2: Vuelve un conjunto nuevo con todos los elementos 
# de los dos conjuntos eliminando los duplicados.

# •3: Actualizar el primer conjunto con elementos 
# que sólo existen en el primer conjunto y no en el
# segundo conjunto.

# •4: Sacar los elementos 30, 40 del primer conjunto.

# •5: Devolver un conjunto de todos los elementos de 
# conjunt1 o conjunt2, pero no de ambos conjuntos.

conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}

# 1
c1=set(conjunto1)
c1.difference_update(conjunto2)

print("\n1:",c1,"\n")

# 2
conjunto1.update(conjunto2)
conjunto1.discard(conjunto1)

print("\n2:",conjunto1,"\n")

# 3

print("\n3:",conjunto1,"\n")
