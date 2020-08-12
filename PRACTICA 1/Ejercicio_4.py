print("Ejercicio 4 - Numero divisible por 2 numeros")
print("********************************************")
numero = int(input("Ingrese un numero: "))
numerox = int(input("Ingrese el primer divisior: "))
numeroy = int(input("Ingrese el segundo divisor: "))

if numero % numerox == 0 and numero% numeroy == 0:
    print(f"true porque {numero} es divisible por  {numerox} y {numeroy}")
elif numero % numerox == 0 and numero % numeroy != 0 :
    print(f"false porque {numero} no es divisible por {numeroy}")
elif numero % numerox !=0 and numero % numeroy == 0:
    print(f"false porque {numero} no es divisible por {numerox}")
elif numero % numerox !=0 and numero % numeroy != 0:
    print(f"false porque {numero} no es divisible ni por {numerox} ni por {numeroy}")

