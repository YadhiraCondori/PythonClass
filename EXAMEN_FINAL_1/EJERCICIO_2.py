print("Ejercicio 2 - Imprimir lista dependiendo el tamaño asignado")
class Matriz():
    def __init__(self):
        self.tamaño = int(input("Ingrese un numero entero: "))
        self.new_lista = []
    def crear_lista(self):
        for i in range(self.tamaño):
            lista  = i
            self.new_lista.append(lista)
        print(self.new_lista)
matriz = Matriz()
matriz.crear_lista()