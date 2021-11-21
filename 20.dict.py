# Se tiene información de 4 personas donde se indica el DNI, 
# el nombre, apellidos y la edad en años de cada persona:
# 17626679 "Pepe Soler" 23
# 20201232 "Sara Cortés" 18
# 17923122 "Juan Bilbao" 18
# 20003609 "María Orante" 19
# Escribe el diccionario llamado personas para guardar la 
# información utilizando el dni como clave y
# los valores serán una tupla de los datos.

mydict = {}
consulta = ""

while True:

    dni=input("\nDona'm el teu DNI[ 0 per a eixir ]: ")
    if dni == "0":
        break
    nom=input("Dona'm el teu nom: ")
    cognom=input("Dona'm el teu cognom: ")
    edad=int(input("Dona'm la teua edad: "))

    dades = [nom+" "+cognom, edad]
    mydict[dni] = dades

print("\nDNIs guardats en la base de dades:")
print(mydict.keys())

while consulta not in mydict.keys():

    consulta=input("\nDona'm un DNI i et donare les dades d'eixa persona: ")

    if consulta not in mydict.keys():
        print("\nDNI incorrecte o no es troba en la base de dades.")

print(),print(mydict[consulta])
