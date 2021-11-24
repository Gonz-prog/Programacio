n, m=int(input("\nDame un valor para 'n'\n")), int(input("\nDame un valor para 'm'\n"))

def productorioN(n,m):
    producto=n*m
    return producto

def sumatorioN(n,m):
    suma=n+m
    return suma

suma=sumatorioN(n,m)
print("\nResultado de la suma",suma)

producto=productorioN(n,m)
print("\nResultado de la multiplicacion",producto)
