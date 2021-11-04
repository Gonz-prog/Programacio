# Programa que dada una frase imprima cada palabra en una 
# línea y nos diga el número de palabras de la frase.

cadena="Hacemos Trekking todos los domingos que podemos"

total=len(cadena.split())

cadena=cadena.split()

for c in cadena:
    
    print(c)

print("Hay",total,"palabras")