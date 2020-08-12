print("ejercicio convetidor")
tipo_de_cambio = 0.28
print ("ingresa el monto en soles")
monto_soles = float(input())
monto_dolares = round(monto_soles * tipo_de_cambio,2)
print("El monto en dolares es: "  + str(monto_dolares))