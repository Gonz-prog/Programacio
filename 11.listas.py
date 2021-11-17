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

x=(3,4,2,5,5,5,2,3)

a=list(x)

a.sort()

y=tuple(a)

print(y)
