# Operaciones con conjuntos (set)  
# •Añadir una lista de elementos a un conjunto:
# Conjunto = {"Programación", "Sistemas", "Inglés"}
# Lista = ["Bases de datos", "Lenguaje de Marcas", "Entornos"]

conjunto = {"Programación", "Sistemas", "Inglés"}
lista = ["Bases de datos", "Lenguaje de Marcas", "Entornos"]

a=list(conjunto)

for i in lista:
    a.append(i)

b=set(a)

print("\n",b,"\n")
