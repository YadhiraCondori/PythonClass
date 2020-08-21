
print("EJERCICIO 1 - COMPARAR RESPUESTAS DE UN EXAMEN")
print("***********************************************")
def listas(lista_1,lista_2):
    print(f"Las respuestas correctas son: {lista_1}" )
    print(f"las respuestas del alumno son: {lista_2}" )
    contador = 0
    for i in range(4):
        
        if lista_1[i] == lista_2[i]:
            contador = contador + 4
        elif lista_2[i] == "":
            contador = contador + 0    
        elif lista_1[i] != lista_2[i]:
            contador = contador - 1
    if contador > 0:
        print("Tu nota final es: " +str(contador))
    else:
        new_contador = contador - contador
        print(f"tu nota final es: {new_contador}")
listas(["a","b","c","d"],["a","b","","e"])
