# Dada una tupla x de números no ordenados, 
# escribimos un programa que cambie la
# asignación de x de manera que el resultado sea una 
# tupla ordenada.
# SUGERENCIA: las tuplas NO tienen método de 
# ordenación, pero las listas sí tienen ...
# """
# Por ejemplo si la tupla es x = (3,4,2,5,5,5,2,3)
# el resultado será:
# """
# (2, 2, 3, 3, 4, 5, 5, 5)

# Iniciar una tupla con valores dentro
x=(3,4,2,5,5,5,2,3)

# Pasar a lista
a=list(x)

# Ordenarla
a.sort()

# Pasar a tupla
y=tuple(a)

# Imprimir
print(y)
