inicio= int(input("inicio:"))
final = int(input("final:"))
for i in range(inicio, final):
    if i%2==0:
        print(i,"es par")
    else:
        print(i,"es impar")