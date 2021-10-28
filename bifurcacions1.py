#Fes un programa que, donades 2 variables enteres, 
#mostre quin és el número més gran i quin el més menut


a=int(input("Donam un nombre: "))
b=int(input("Donal altre nombre: "))

if a>b:
    print(a," Es mes gran que ",b)
    

elif b>a:
    print(a," Es mes menut que ",b)

else: 
    print(a," i ",b," son iguals")