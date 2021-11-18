# Dada la cadena
# s="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"
# Crea un programa que inserte los elementos que están separados por «|» 
# en una lista.
# Sabiendo que la lista creada sólo tiene cuatro elementos diferentes 
# (es decir, «manzana», «pera»,«cereza» y «fresa»), 
# creará otra lista donde cada elemento sea una tupla con el nombre 
# de la fruta y su multiplicidad (es decir, el número de veces que 
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
s3=[]

s0="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"

s1=list(s0.split("|"))

for i in s1:
    s2=[]
    s2.append(i)
    s2.append(s1.count(i))

    s3.append(s2)

s4=list(s3)
s5=list(s4)

print("\ncuenta =",s5,"\n")
