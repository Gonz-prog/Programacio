#Fes un programa que, donades 3 variables enteres, 
#mostre quin és el número més gran

a=int(input("Donam un nombre: "))
b=int(input("Donam el segon nombre: "))
c=int(input("Donam el tercer nombre: "))

if a>b and a>c:
    print(a," Es el nombre mes gran")

elif b>a and b>c:
    print(b," Es el nombre mes gran")

elif c>a and c>b:
    print(c," Es el nombre mes gran")

elif a==b and a==c:
    print("Tots els nombres son iguals")