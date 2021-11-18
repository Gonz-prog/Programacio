#Programa que dada una tupla x generará otra tupla que 
#contendrá:
#•al principio, los mismos elementos de x excepto el último.
#•al final, los elementos «d» y «e».
#Su código debería funcionar con cualquier tupla x.
#"""
#Por ejemplo si la tupla es x = ( 'a', 'b', 'c')
#el resultado será:
#"""
#x = ('a', 'b', 'c')
#y = ('a', 'b', 'd', 'e')

#Crear la tupla
x=("a", "b", "c")

#Convertir en lista
a=list(x)

#Quitar último elemento
a.remove(a[-1])

#Añadir dos elementos al final
a.append("d")
a.append("e")

#Crear la tupla a partir de una lista
y=tuple(a)

#Imprimir
print("\nx =",x,"\n\ny =",y,"\n")
