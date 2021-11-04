#Programa para comparar si dos palabras, introducidas por el usuario, 
# son iguales. Comoresultado mostrará:
#•Si las palabras son exactamente iguales
#•Si las palabras son iguales (sin tener en cuenta mayúsculas y minúsculas)
#•O si las palabras son totalmente diferentes

cadena1, cadena2=(input("Dame la primera palabra: ")), (input("Dame la segunda palabra: "))

if cadena1 in cadena2:
    print("Son exactamente iguales")

cadena1, cadena2=cadena1.lower(), cadena2.lower()

if cadena1 in cadena2:
    print("Son iguales (sin tener en cuenta mayúsculas y minúsculas)")

elif cadena1 not in cadena2:
    print(cadena1,"y",cadena2,"son diferentes")
