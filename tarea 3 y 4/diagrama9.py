print("Teclée argumento x?")
x = float(input())
while x <= -1 or x >= 1:
    print("Error, valor de x inválido")
    print("Teclée argumento x?")
    x = float(input())
print("Hasta cuantos términos de la serie:")
n = int(input())
suma = 0
i = 1
potencia = x
signo = 1
while i <= n:
    suma = suma + signo * potencia / i
    potencia = potencia * x
    signo = signo * -1
    i = i + 1
print("ln(1+x) = " + str(suma))
