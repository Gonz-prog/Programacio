print("Suma")

a=int(input("Donam el primer nombre: "))
b=int(input("Donam el segon nombre: "))

suma=a+b

print("La suma es",suma)

print("Intercambiar")

a=float(input("Introduce el valor de la variable a:"))
b=float(input("Introduce el valor de la variable b: "))

aux=a
a=b
b=aux

print("El valor de a es",a)

print("El valor de b es",b)

print("Intercambi²")

a=float(input("Donam el primer nombre: "))
b=float(input("Donam el segon nombre: "))
c=float(input("Donam el tercer nombre: "))

b=a
a=c
c=b

print("El valor de a es",a)
print("El valor de b es",b)
print("El valor de c es",c)

print("Suma amb 3 decimals")

a=float(input("Donam el primer nombre: "))
b=float(input("Donam el segon nombre: "))
c=float(input("Donam el tercer nombre: "))
d=float(input("Donam el cuart nombre: "))

suma=float(a+b+c+d)

print("El resultat de la suma es %6,3f"%suma)

print("")