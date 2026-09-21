print("Dame un número para verificar si es perfecto:")
numero = int(input())
while numero != 0:
    if numero < 0:
        print("El " + str(numero) + " no es positivo")
    else:
        suma = 0
        divisor = 1
        while divisor < numero:
            if numero % divisor == 0:
                suma = suma + divisor
            divisor = divisor + 1
        if suma == numero:
            print("El " + str(numero) + " sí es perfecto")
        else:
            print("El " + str(numero) + " no es perfecto")
    print("Dame un número para verificar si es perfecto:")
    numero = int(input())
print("Fin de algoritmo")
