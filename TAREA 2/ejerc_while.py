print("Ejercicio - Limite de intentos  / password: 123")
contador = 0
password = 123
while contador < 3:
    contraseña = int(input("Ingrese su contraseña: "))
    if contador < 2:
        if password == contraseña:
            print("Bienvenido")
            break
        else:
            print("Error, Ingrese otra contraseña: ")
    else:
        print("Demasiados intentos")
    contador = contador + 1
