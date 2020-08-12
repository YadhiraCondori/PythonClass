mensaje = """" 
hola, este es un conversor de monedas.
ingresa cualquiera de estas 3 opciones
1 = Soles- Dolares
2 = Eurors - Dolares
3 = Pesos Colombianos - Dolares"""
print(mensaje)
opcion = int(input("Ingrese la opcion: "))
if opcion == 1:
    print(f"has escogido la opcion {opcion}")
    monto_soles= float(input("Ingrese la cantidad en soles: "))
    monto_dolares = round(monto_soles * 0.28,2)
    print("la cantidad en dolares es: " + str(monto_dolares))
elif opcion == 2:
    print(f"has escogido la opcion {opcion}")
    monto_euros= float(input("Ingrese la cantidad en euros: "))
    monto_dolares = round( monto_euros * 1.18,2) 
    print("la cantidad en dolares es: " + str(monto_dolares))
elif opcion == 3:
    print(f"has escogido la opcion {opcion}")
    monto_pesos_colombianos= float(input("Ingrese la cantidad en pesos colombianos: "))
    monto_dolares =round(monto_pesos_colombianos * 0.00027,2)  
    print("la cantidad en dolares es: " + str(monto_dolares))

    


