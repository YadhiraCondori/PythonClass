print("EJERCICIO 1 - INGRESAR 2 LISTAS E IMPRIMIR EL NUMERO MAYOR DE CADA LISTA")
def listas (lista1):
    new_lista = []
    contador = 0
    producto = 1
    print(lista1)
    while contador < len(lista1):
        for i in range(1):
            if lista1[i+contador][i] < lista1[i+contador][i+1]:
                agregar_valor = lista1[i+contador][i+1]
                new_lista.append(agregar_valor)
            
            else:
                agregar_valor = lista1[i+contador][i]
                new_lista.append(agregar_valor)
        contador = contador + 1
    for j in new_lista:
        producto = producto * j
    print(f"La multiplicacion de los numeros {new_lista} es {producto}")
listas([[40,20],[4,5],[2,4],[5,4],[1,2]])