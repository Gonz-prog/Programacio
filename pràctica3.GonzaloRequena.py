#Fer un programa que donades 3 variables (del tipus que siguin) 
#intercanvie els seus valors de la següent manera


a=float(input("Donam el primer nombre: "))
b=float(input("Donam el segon nombre: "))
c=float(input("Donam el tercer nombre: "))

b=a
a=c
c=b

print("El valor de a es ",a)
print("El valor de b es ",b)
print("El valor de c es ",c)