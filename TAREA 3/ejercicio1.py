print("Cantidad de numeros impares")
cant_impares = 0
for i in range(100):
    if i % 2 != 0:
        print(i)
        cant_impares = cant_impares + 1
print("La cantidad de números impares es: "+ str(cant_impares))
