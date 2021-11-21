# Se tiene información de 4 personas donde se indica el DNI, 
# el nombre, apellidos y la edad en años de cada persona:
# 17626679 "Pepe Soler" 23
# 20201232 "Sara Cortés" 18
# 17923122 "Juan Bilbao" 18
# 20003609 "María Orante" 19
# Escribe el diccionario llamado personas para guardar la 
# información utilizando el dni como clave y
# los valores serán una tupla de los datos.

dict = {}
cadena = ""

while True:

    dni=input("\nDime tu DNI[ 0 para salir ]: ")
    if dni == "0":
        break
    nombre=input("Dime tu nombre: ")
    apellido=input("Dime tu apellido: ")
    edad=int(input("Dime tu edad: "))

    datos = [nombre+" "+apellido, edad]
    dict[dni] = datos

print("\nDNI guardados en la base de datos:")
print(dict.keys())

while cadena not in dict.keys():

    cadena=input("\nDime un DNI y te digo los datos de esa persona: ")

    if cadena not in dict.keys():
        print("\nDNI incorrecto o no se encuentra en la base de datos.")
print()
print(dict[cadena],"\n")
