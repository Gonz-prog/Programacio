#implementar un programa que calcule la temperatura 
#en graus Celsius a partir de la temperatura
#en graus Fahrenheit. La fórmula es la següent

f=float(input("Quina temperatura fa avuí? En Fahrenheit? "))

c=float(5/9*(f-32))

print(f," Fº = %3.2f"%c," Cº")