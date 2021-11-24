texto=''
print("\nDime tres valores para 'a, b, c' y te digo que triángulo se puede hacer\n")
a, b, c=int(input("a: ")), int(input("b: ")), int(input("c: "))

if a<(b+c) and b<(a+c) and c<(a+b):
        texto='Con '+str(a)+','+str(b)+','+str(c)+' si se puede hacer un triangulo '
elif a == b == c:
    texto+='Equilatero'
elif a == b or b == c or a == c:
    texto+='Isósceles'
else:
    texto+='Escaleno'

print(texto)
