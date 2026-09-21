producto = 1
numerador = 2
denominador = 1
print("numero de terminos:")
terminos = int(input())
while terminos <= 0:
    print("error, el numero debe ser mayor a cero")
    print("numero de terminos?")
    terminos = int(input())
i = 1
while i <= terminos:
    producto = producto * numerador / denominador
    if i % 2 == 0:
        numerador = numerador + 2
        denominador = denominador + 2
    i = i + 1
resultado = producto * 2
print("Valor aproximado de pi = " + str(resultado))
