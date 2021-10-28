import math

#Fes un programa que calcule les solucions reals 
#de l’equació de 2n grau ax2+ bx + c = 0, amb
#la famosa fórmula
#x = −b ±√b2−4ac/2a

a=int(input("Donam un valor per a la a: "))

b=int(input("Donam un valor per a la b: "))

c=int(input("Donam un valor per a c: "))

arrel=b*b-4*a*c

if arrel>=0:

    x1=(-b+math.sqrt(b*b-4*a*c))/2*a

    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
    
    print("Ara a calcular ax2+ bx + c = 0")

    print(x1,"es el resultat positiu")

    print(x2,"es el resultat negatiu")
else:
    print("No te solució amb aquestes dades")