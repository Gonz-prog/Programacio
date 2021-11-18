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
añadir0=[]

# Cadena
cadena="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"

# Crear la lista palabras a partir de la cadena quitando el separador con .split("|")
palabras=list(cadena.split("|"))

# Inicio del bucle que añadirá i más el número de carácteres en la lista contar 
for i in palabras:
    contar=[]
    contar.append(i)
    contar.append(palabras.count(i))
    
    # Inicio del bucle en el rango de la lista palabras 
    for i in range(len(palabras)):
        
        # Pasar a tupla
        contar=tuple(contar)
    añadir0.append(contar)
    añadir=tuple(añadir0)
    añadir1=list(añadir0)

print("\ncuenta =",añadir1,"\n")
