print("dame un numero:")
n = int(input())
while n <= 0:
    print("el numero debe ser positivo")
    print("dame un numero:")
    n = int(input())
f = 0
x = 1
print(f)
while x <= n:
    f = 2 * f + x * x
    print(f)
    x = x + 1
