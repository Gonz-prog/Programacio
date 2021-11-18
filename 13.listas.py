# Dada la cadena
# s="manzana|pera|manzana|cereza|pera|manzana|pera|pera
# |cereza|pera|fresa"
# Crea un programa que inserte los elementos que están 
# separados por «|» en una lista.
# Sabiendo que la lista creada sólo tiene cuatro 
# elementos diferentes (es decir, «manzana», «pera»,
# «cereza» y «fresa»), creará otra lista donde cada 
# elemento sea una tupla con el nombre de la fruta y su multiplicidad (es decir, el número de veces que
# aparece en la lista original).
# Imprimirá el contenido de cada tupla en una línea independiente 
# (es decir, en la primera línea: la «manzana» está presente 3 veces).
# """
# El resultado será:
# """
# cuenta = [("manzana", 3), ("pera", 5), ...] [("manzana", 3), ("pera", 5), ("cereza", 2), ("fresa", 1)]
# la manzana está presente 3 veces
# la pera está presente 5 veces
# la cereza está presente 2 veces
# la fresa está presente 1 vez

# Introducir lista
lista=[]
nocopy=[]

# Cadena
cadena="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"

# Crear la lista palabras a partir de la cadena quitando el separador con .split("|")
palabras=list(cadena.split("|"))

for i in palabras:

    if i not in nocopy:
        nocopy.append(i)
        contar=[]
        contar.append(i)
        contar.append(palabras.count(i))
        añadir=tuple(contar)
        lista.append(añadir)


print(lista)

for i in lista:
    print("La",i[0],"está presente",i[1],"veces")
