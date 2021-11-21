# Programa para leer una cadena y devolver un diccionario 
# con la cantidad de apariciones
# de cada palabra en la cadena.
# Por ejemplo, para la cadena:
# "qué tema y qué ejercicio estás haciendo"
# debe devolver:
# "qué" : 2, 'tema': 1, 'y': 1, ejercicio ': 1,'estás ': 1, "haciendo": 1

dictionari = {}

frase0=input("\nIntroduce una frase\n")

frase1=frase0.split()

for i in range(len(frase1)):
    c=0
    for y in range(len(frase1)):
        if frase1[i] == frase1[y]:
            c+=1
    dictionari.update({frase1[i]: c})
print()
print(dictionari,"\n")
