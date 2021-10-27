#Implementar un programa que calcule els interessos produïts 
#i el capital acumulat d’una quantitat c invertida a un interès r 
#(expressat en tant per cent) durant t dies. La fórmula per al 
#càlcul d’interessos és:

c=float(input("Quantitat d'€ invertida: "))
r=float(input("Quantitat interés en %: "))
t=float(input("Quantitat dies: "))

i=float(c*r*t/36000)

print("Interesos aconseguits en €: ",i)