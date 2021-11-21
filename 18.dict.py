# Programa para hacer un seguimiento de las fechas de 
# cumpleaños de nuestros amigos, la información está 
# guardada por nombre y podemos encontrarla, por tanto, 
# en función de ese nombre.
# Crear un diccionario de nombres y aniversarios (al menos 5).
# Al ejecutar el programa, tendrá que pedir al usuario que 
# introduzca un nombre para que le devuelva elaniversario de 
# ese amigo.

dict0 = {
    "Gonzalo": "7 Abril",
    "Seida": "13 Decembre",
    "Gemma": "30 Agost",
    "Mariam": "15 Abril",
    "Nayala": "21 Octubre",
    "Ainhoa": "14 Abril",
    "Francesc": "24 Juliol",
}
while True:
    nom=input("\nDime el nombre y te digo el aniversario ('s' para salir)\n")

    x=dict0.keys()

    if nom in x:
        print(dict0[nom])
    elif nom == "s":
        print("\nHasta gracias y muchas nunca\n")
        break
    else:
        print("\n'ERROR: Introduce un nombre válido'\n",x)
