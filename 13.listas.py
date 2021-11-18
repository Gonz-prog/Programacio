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

añadir0=[]

cadena="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"

palabras=list(cadena.split("|"))

for i in palabras:
    contar=[]
    contar.append(i)
    contar.append(palabras.count(i))

    for i in range(len(palabras)):
        contar=tuple(contar)
    añadir0.append(contar)
    añadir1=list(añadir0)

print("\ncuenta =",añadir1,"\n")
