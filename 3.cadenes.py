# Programa para comparar si dos palabras, introducidas por el usuario, 
# son iguales. Como resultado mostrará:
# •Si las palabras son exactamente iguales
# •Si las palabras son iguales (sin tener en cuenta mayúsculas y minúsculas)
# •O si las palabras son totalmente diferentes

# Introducir datos (str)
cadena1, cadena2=(input("Dame la primera palabra: ")), (input("Dame la segunda palabra: "))

# Comprovar si son exáctamente iguales
if cadena1 in cadena2:
    print("Son exactamente iguales")

# Cambiar a minúsculas 
cadena1, cadena2=cadena1.lower(), cadena2.lower()

# Comprobar si son iguales (sin tener en cuenta mayúsculas y minúsculas) e imprimir
if cadena1 in cadena2:
    print("Son iguales (sin tener en cuenta mayúsculas y minúsculas)")

# Comprovar si son diferentes
elif cadena1 not in cadena2:
    print(cadena1,"y",cadena2,"son diferentes")
