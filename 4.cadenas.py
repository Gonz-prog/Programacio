# Programa para validar direcciones de correo electrónico 
# mientras el usuario lo necesite. Partiendo de una dirección 
# de correo como «alumne@ieseljust.com» podemos identificar la cuenta
# de usuario como alumno y el dominio ieseljust.com. El programa debe 
# indicar si la dirección que le introduce el usuario es una dirección 
# válida y separar el usuario del dominio para escribir como

#resultado:
#•Usuario: alumne
#•Servidor: ieseljust.com

cadena=(input("Introduce tu dirección de correo electrónico: "))

separador="@"

if separador in cadena:
    direccion=cadena.split("@")
    print("Usuario: ",direccion[0])
    print("Servidor: ",direccion[1])
else:
    print("Email sin @")