temporal = 0
print("dame el primer numero entero positivo:")
numero1 = int(input())
print("dame el segundo numero entero positivo:")
numero2 = int(input())
if numero1 > numero2:
    temporal1 = numero1
    numero1 = numero2
    numero2 = temporal
suma = 0
i = numero1
while i <= numero2:
    if i % 2 != 0:
        suma = suma + i
    i = i + 1
print("La suma de los números impares entre los números que me diste es: " + str(suma))
