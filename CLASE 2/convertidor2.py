mensaje = """
hola, este es un conversion de monedas
Ingresa cualquiera de estas 3 opciones
1 = soles - dolares
2 = euros - dolares
3= pesos colombianos - dolares
"""
print(mensaje)
opcion = int(input("Ingresa la opcion: "))
if opcion == 1:
    tipo_de_cambio = 0.28
    monto = float(input("hola, ingresa tu monto en soles: "))
    monto_dolares = round(monto * tipo_de_cambio,2)
    print(monto_dolares)
elif opcion == 2:
    tipo_de_cambio = 1.19
    monto = float(input("hola, ingresa tu monto en euros: "))
    monto_dolares = round(monto * tipo_de_cambio,2)
    print(monto_dolares)
elif opcion == 3:
    tipo_de_cambio = 0.00027 
    monto = float(input("hola, ingresa tu monto en pesos colombianos: "))
    monto_dolares = round(monto * tipo_de_cambio,2)
    print(monto_dolares)    
