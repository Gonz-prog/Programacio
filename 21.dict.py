# Programa que tiene guardado, en un diccionario, 
# el código Morse correspondiente a todos
# los caracteres. Escribir un programa que lea una 
# cadena y, según corresponda, la traducirá del alfabeto
# al código morse, o del código morse al alfabeto.

morse = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....',
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.',
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-',
    'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-',
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.',
    ',':'--..--', 
    '.':'.-.-.-',
    '?':'..--..', 
    '/':'-..-.', 
    '-':'-....-',
    '(':'-.--.',
    ')':'-.--.-',
    ' ':'/'
}

print(
    "\nXxx---------------------------------xxX\n"
    "¡¡¡Bienvenidos al traductor de Morse!!!"
    "\nXxx---------------------------------xxX\n"
)

tr0=input("Introduce una frase para traducir a Morse\n")

llaves=morse.keys()
valores=morse.values()

# is not morse --> need letters --> "A"
# is morse --> need words --> ".-"

letras=list(tr0)
palabras=tr0.split(" ")

# is not morse
if letras[0].isalpha():
    for i in letras:
        print(morse[i.upper()],end=" ") # del dyct morse donam el valor de la clau [i]
    print()

# is morse
else:
    for i in palabras:
        for clau,valor in morse.items():
            if i == valor:
                print(clau.lower(),end="")
print("\n")
