# Determina si los dos conjuntos siguientes tienen 
# o no elementos en común. Si es así,
# muestra los elementos comunes:

conjunto1 = {210, 200, 301, 40, 70, 32}
conjunto2 = {101, 7, 140, 30, 200, 40}

c1=set(conjunto1)
c1.update(conjunto2)

print("\n",c1,"\n")
