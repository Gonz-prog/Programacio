#Calcula el valor del polinomi: ax5−bx3+cx −d,
#sent els valors de a, b, c, d variables introduïdes
#per teclat. Comprova els valors amb l’exercici 9.


x=float(input("Donam el valor de la x: "))
a=float(input("Donam el valor de a: "))
b=float(input("Donam el valor de b: "))
c=float(input("Donam el valor de c: "))
d=float(input("Donam el valor de d: "))


resultat=float(a*x**5)-float(b*x**3)+float(c*x)-float(d)

print("El resultat del polinomi ax⁵-bx³+cx-d es: ",resultat)