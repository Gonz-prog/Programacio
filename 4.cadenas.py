# Programa para validar direcciones de correo electrónico 
# mientras el usuario lo necesite. Partiendo de una dirección 
# de correo como «alumne@ieseljust.com» podemos identificar la cuenta
# de usuario como alumno y el dominio ieseljust.com. El programa debe 
# indicar si la dirección que le introduce el usuario es una dirección 
# válida y separar el usuario del dominio para escribir como

#resultado:
#•Usuario: alumne
#•Servidor: ieseljust.com

# Iniciar el bucle para que no pare de pedir datos  
# hasta que se vea cumplido, entonces saltará al esle:
while True:

    # Introducir str
    email=(input("Introduce un email\n"))
    
    # Comporbrar si hay una @ en el str, si no
    # dará error print("Introduce un email valido, xxx@xxx.xxx")
    if "@" not in email or "." not in email:
        print("Introduce un email valido, xxx@xxx.xxx")
    
    # Si la anterior condición no se cumple
    # separaremos el str por la @ indicando 
    # las dos posiciones del .split("@")[0] .split("@")[1]
    else:
        usuario=email.split("@")[0]
        servidor=email.split("@")[1]
        
        # Comprovamos que en estas dos posiciones hay un str
        if len(usuario) == 0 or len(servidor) == 0:
            print("Introduce un email valido, xxx@xxx.xxx")
        
        # Si la anterior condición no se cumple
        # separaremos el str "servidor" por el . indicando 
        # las dos posiciones del .split(".")[0] .split(".")[1]
        else:
            com1=servidor.split(".")[0]
            com2=servidor.split(".")[1]
            
            # Comprovamos que en los dos lados del str "servidor"
            # haya un str
            if len(com1) == 0 or len(com2) == 0:
                print("Introduce un email valido, xxx@xxx.xxx")
            
            # Si ninguna comprobación da error, entonces 
            # saldrá del while para imprimir 
            # la primera separacón que se hizo
            else:
                break
print("\nUsuario: ",usuario)    
print("Servidor: ",servidor)
