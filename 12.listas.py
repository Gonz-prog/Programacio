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

resultado=[]

animales = "gato, perro, canario, pescado, conejo, hámster"

x=list(animales.split(", "))

for i in x:
    valores=[]
    valores.append(i)
    valores.append(len(i))

    y=tuple(valores)
    resultado.append(y)

final=tuple(resultado)
print(final)
