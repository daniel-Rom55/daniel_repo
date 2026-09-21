print("dame un numero entero positivo:")
numero = int(input())
suma = 0
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        suma = suma + divisor
    divisor = divisor + 1
