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

# Crear la tupla
lista1=[]
t=('C', 'h', 'R', 'm', 'A', 's', 'M', 'o', 'T', 'y', 'C ')

# Convertir en lista
lista0=list(t)

# Inicio del bucle que comprobará si cada str de la lista0 es .upper()
for i in range(len(lista0)):
    if lista0[i] == lista0[i].upper():
        
        # Insertar a la lista los str que indique i
        lista1.append(lista0[i])

# Inicio del bucle que comprobará si cada str de la lista0 es .lower()
for i in range(len(lista0)):
    if lista0[i] == lista0[i].lower():
        
        # Insertar a la lista los str que indique i
        lista1.append(lista0[i])

# Pasar a tupla
res=tuple(lista1)

print(res)
