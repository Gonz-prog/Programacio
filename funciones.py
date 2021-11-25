def sumar(a,b):
    return a+b

def listar(nom):
    lista=[]
    lista.append(nom)
    return lista

def areaRectangle(base,altura):
    return base*altura

def media(lista):
    suma=0
    for i in lista:
        suma+=i
    media=suma/len(lista)
    return media
