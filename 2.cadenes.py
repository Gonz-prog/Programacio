# Programa que dada una frase imprima cada palabra en una 
# línea y nos diga el número de palabras de la frase.

#Itroducir cadena
cadena="Hacemos Trekking todos los domingos que podemos"

# Separar palabra por el separador 
# .split() en este caso un espacio
# y contar al mismo tiempo las palabras 
total=len(cadena.split())

cadena=cadena.split()

# Recorrer el str imprimiendo cada palabra 
for c in cadena:
    
    print(c)

# Imprimir el número de palabras
print("Hay",total,"palabras")
