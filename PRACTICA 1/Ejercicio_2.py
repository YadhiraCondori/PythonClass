print("Ejercicio 2 - Area/Perimetro de un poligono")
print("********************************************")

mensaje = """Elija una de estas 2 opciones:
1 = Area del Cuadrado
2 = Perimetro del Rectangulo"""

print(mensaje)
opcion = int(input("Ingrese una opción: "))

def area_poligono ():  
    print("Area de un cuadrado")
    longitud = float(input("Ingrese la Longitud del poligono: "))
    print("Hallando area del cuadrado...")
    area_cuadrado = longitud ** 2
    print("El area del cuadrado es: "+str(area_cuadrado))
def perimetro_poligono():
    print("Perimetro de un rectangulo")
    longitud = float(input("Ingrese la Longitud del poligono: "))
    ancho = float(input("Ingrese el ancho del poligono: "))
    print("Hallando perimetro...")
    perimetro = 2*(longitud + ancho)
    print("El perimetro del rectángulo es :"+str(perimetro))

if opcion == 1:
    area_poligono()
elif opcion == 2:
    perimetro_poligono()
else:
    print(f"la opcion {opcion} no existe, intente nuevamente")

    


