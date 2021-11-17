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

x=("a", "b", "c")

a=list(x)

a.remove(a[-1])

a.append("d")
a.append("e")

y=tuple(a)

print("\nx =",x,"\n\ny =",y,"\n")
