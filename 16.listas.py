# Determina si los dos conjuntos siguientes tienen 
# o no elementos en común. Si es así,
# muestra los elementos comunes:

conjunto1 = {210, 200, 301, 40, 70, 32}
conjunto2 = {101, 7, 140, 30, 200, 40}

c1=conjunto1.intersection(conjunto2)

print("\nElementeos en comun:",c1,"\n")

# •Modificar el programa para que pida los conjuntos a comparar.

while True:

    x, y=input("Introduce valores para el conjunto1 o 's' para salir\n"), input("Introduce valores para el conjunto2 o 's' para salir\n")
    if x == "s" and y == "s":
        break

    a=set(x)
    b=set(y)   

    for i in a:
        c2=a.intersection(y)

print("Resultado al comparar:",c2)
