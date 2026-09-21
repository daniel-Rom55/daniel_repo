print("Dame el número n1: ")
n1 = float(input())

print("Dame el número n2: ")
n2 = float(input())

print("Dame el número n3: ")
n3 = float(input())

if n1 <= 0 or n2 <= 0 or n3 <= 0:
    print("Alguno o varios de los números no son positivos")
else:
    s1 = int(n1) + round((n1 - int(n1)) * 10000)
    s2 = int(n2) + round((n2 - int(n2)) * 10000)
    s3 = int(n3) + round((n3 - int(n3)) * 10000)

    print("La suma resultante de n1 =", s1)
    print("La suma resultante de n2 =", s2)
    print("La suma resultante de n3 =", s3)

    mayor = max(max(s1, s2), s3)

    print("El valor mayor de las sumas es", mayor)