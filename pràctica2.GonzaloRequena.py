#Donades dues variables a i b reals, fer un programa
#que intercanvie els valors de les mateixes

a=float(input("Introduce el valor de la variable a: "))
b=float(input("Introduce el valor de la variable b: "))

aux=a
a=b
b=aux

print("El valor de a es ",a)
print("El valor de b es ",b)