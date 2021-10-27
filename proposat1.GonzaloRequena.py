# Fes un programa que, donades 2 variables enteres,
# mostre quin és el número més gran i quin el més menut.

a = int(input("Donam el valor de a: "))
b = int(input("Donam el valor de b: "))

if a < b:
    print(b, " es mes gran que ", a)
else:
    print(a, " es mes gran que ", b)
