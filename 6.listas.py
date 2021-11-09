 # Crear un programa que pida al usuario un número 
 # de mes (por ejemplo, el 5) y diga cuántos días 
 # tiene (por ejemplo, 31) y el nombre del (mayo). 
 # Se deben utilizar listas y supondremos que febrero
 # tiene 28 días.

meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num1=int(input("Dame el numero de un mes: "))

if num1 < 13:

    if num1 == 1:
        print("Mes: ",meses[0])
        print("Dias: ",dias[0])