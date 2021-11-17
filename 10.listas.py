#Programa que Dada una tupla con caracteres 
#mayúsculas/minúsculas alternativos, modi-
#fique la asignación de la tupla de manera 
#que sea una tupla con todos los caracteres 
#en mayúscula en primera posición y todos los 
#caracteres en minúscula en las posiciones finales.
#"""
#Por ejemplo si la tupla es 
#t = ( 'C', 'h', 'R', 'm', 'A', 's', 'M', 'o', 'T', 'y', 'C ')
#el resultado será:
#"""
#("C", "R", "A", "M", "T", "C", "h", "m", "s", "o", "y")

lista1=[]
t=('C', 'h', 'R', 'm', 'A', 's', 'M', 'o', 'T', 'y', 'C ')

lista0=list(t)

for i in range(len(lista0)):
    if lista0[i] == lista0[i].upper():

        lista1.append(lista0[i])

for i in range(len(lista0)):
    if lista0[i] == lista0[i].lower():

        lista1.append(lista0[i])

res=tuple(lista1)

print(res)
