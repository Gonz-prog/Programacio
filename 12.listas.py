# Programa que dada una cadena de animales como 
# por ejemplo: 
# animales = "gato, perro, canario, pescado, conejo, hámster"
# •Creará una tupla de tuplas donde cada tupla tenga dos 
# elementos: el nombre del animal y la
# longitud del nombre, es decir 
# (("perro", 5), ("hámster", 7))
# •Imprimirá la tupla
# """
# Por ejemplo si la tupla es 
# (gato, perro, canario, pez, conejo, hámster)
# el resultado será:
# """
# (("Gato", 4), ("perro", 5), ("canario", 7), ("pez", 3), ("conejo", 6), ("hámster", 7))

# Iniciar lista
resultado=[]

# Cadema
animales = "gato, perro, canario, pescado, conejo, hámster"

# Convertir la cadena en lista quitando el separador
x=list(animales.split(", "))

# Inicio del bucle que le dará cada palabra y su valor a la lista valores
for i in x:
    valores=[]
    valores.append(i)
    valores.append(len(i))
    
    # Crear una tupla a partir de valores
    y=tuple(valores)
    
    # Añadir a la lista resultado los valores de la tupla y
    resultado.append(y)

# Crear una tupla a partir de resultado e imprimir
final=tuple(resultado)
print(final)
