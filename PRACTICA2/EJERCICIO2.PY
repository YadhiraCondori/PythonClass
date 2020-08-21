import random
print("EJERCICIO 2 - Escribir una funcion que me devuelva una lista")
print("************************************************************")

def lista():
    nombre = input("Ingrese una palabra: ")
    convertir_lista = []
    contador = 0
    for i in nombre:
        contador = contador + 1
        convertir_lista.append(i)
    if contador < 2:
        print("Invalid String, no se permiten menos de 2 caracteres")
    elif contador < 100:
        print(f"la palabra {nombre} en una lista reducida es: {convertir_lista[1::2]}")
    elif contador > 100:
        print("Invalid String, no se permiten mas de 100 caracteres")
lista()

