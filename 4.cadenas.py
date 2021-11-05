# Programa para validar direcciones de correo electrónico 
# mientras el usuario lo necesite. Partiendo de una dirección 
# de correo como «alumne@ieseljust.com» podemos identificar la cuenta
# de usuario como alumno y el dominio ieseljust.com. El programa debe 
# indicar si la dirección que le introduce el usuario es una dirección 
# válida y separar el usuario del dominio para escribir como

#resultado:
#•Usuario: alumne
#•Servidor: ieseljust.com

while True:

    email=(input("Introduce un email\n"))

    if "@" not in email or "." not in email:
        print("Introduce un email valido, xxx@xxx.xxx")
    else:
        usuario=email.split("@")[0]
        servidor=email.split("@")[1]
        if len(usuario) == 0 or len(servidor) == 0:
            print("Introduce un email valido, xxx@xxx.xxx")
        else:
            com1=servidor.split(".")[0]
            com2=servidor.split(".")[1]
            if len(com1) == 0 or len(com2) == 0:
                print("Introduce un email valido, xxx@xxx.xxx")
            else:
                break
print("\nUsuario: ",usuario)    
print("Servidor: ",servidor)
