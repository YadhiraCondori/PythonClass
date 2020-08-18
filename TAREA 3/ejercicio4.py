print("Cantidad de veces que aparece una letra")
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese letra a buscar: ")
cant_palabras = 0
for i in palabra:
    if i == letra:
        cant_palabras = cant_palabras + 1
print(f"la letra {letra} se repite {cant_palabras}")
        