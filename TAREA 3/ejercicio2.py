print("Cantidad de numeros nultiplos de 3")
cant_multiplos3 = 0
for i in range(100):
    if i % 3 == 0:
        print(i)
        cant_multiplos3 = cant_multiplos3 + 1
print("La cantidad de multiplos de 3 es: "+ str(cant_multiplos3))
