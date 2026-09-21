import math

altura = input("Ingrese Altura: ")
H = float(altura)

ancho = input("Ingresa el Ancho: ")
W = float(ancho)

X = H / W

S = 2 * W * (math.sqrt(X*2 + 1/16) + (1/(16*X)) * (math.log(X + math.sqrt(X*2 + 1/16)) + math.log(4)))

print(f"La longitud de la parabola es:{S}")