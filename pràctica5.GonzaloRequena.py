#Fer un programa que demane dos números i 
#mostre per pantalla la suma, resta,
#producte i divisió, amb 4 decimals.


a=float(input("Donam el primer nombre: "))
b=float(input("Donam el segon nombre: "))

suma=float(a+b)
resta=float(a-b)
producte=float(a*b)
divisio=float(a/b)

print("El resultat de la suma es %6.4f"%suma)
print("El resultat de la resta es %6.4f"%resta)
print("El resultat del producte es %6.4f"%producte)
print("El resultat de la divisio es %6.4f"%divisio)