mensaje = """" 
hola, este es un conversor de monedas.
ingresa cualquiera de estas 3 opciones
1 = Soles- Dolares
2 = Eurors - Dolares
3 = Pesos Colombianos - Dolares"""
print(mensaje)
opcion = int(input("Ingrese la opcion: "))

def monto_total():
    print(f"Usted a escogido la opcion {opcion}")
    monto = float(input("Ingrese su monto: "))
    monto_dolares = round(monto * tipo_cambio,2)
    print("El monto total es: " + str(monto_dolares),"dolares")
if opcion == 1:
    tipo_cambio = 0.28
    monto_total()
elif opcion == 2:
    tipo_cambio = 1.18
    monto_total()
elif opcion == 3:
    tipo_cambio = 0.00027
    monto_total()
else:
    print(f"la opcion {opcion} no se encuentra registrada en la lista")


    
    

