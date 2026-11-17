# =====================================================
# UNIVERSIDAD AUTONOMA DE ZACATECAS
# INGENIERIA DE SOFTWARE
# INTRODUCCION A LA PROGRAMACION
# DOCENTE: El tremendo ChagoUaz_IA
#
# PRACTICA: LISTAS, CENTINELA Y METODO SORT()
# =====================================================
# Funcion para llenar la lista
def llenar_lista(lista):
	print("\n--- LLENAR LISTA ---")
	print("Ingrese numeros reales.")
	print("Escriba FIN para terminar la captura.")
	while True:
		dato = input("Numero (o FIN): ").strip()
		# Verificar el centinela
		if dato.upper() == "FIN":
			print("Captura finalizada.")
			break
		# Validar el numero real
		try:
			numero = float(dato)
			# Rechazar valores no finitos
			import math
			if not math.isfinite(numero):
				print("Error: ingrese un numero finito.")
				continue
			lista.append(numero)
			print("Numero agregado correctamente.")
		except ValueError:
			print("Error: ingrese un numero valido o FIN.")
# Funcion para mostrar la lista
def mostrar_lista(lista):
	print("\n--- CONTENIDO DE LA LISTA ---")
	if len(lista) == 0:
		print("La lista esta vacia.")
	else:
		print("Cantidad de elementos:", len(lista))
		for i, numero in enumerate(lista, start=1):
			print(f"Elemento {i}: {numero}")
# Funcion para ordenar la lista
def ordenar_lista(lista):
	print("\n--- ORDENAR LISTA ---")

	if len(lista) == 0:
		print("No hay elementos para ordenar.")
	else:
		lista.sort()
		print("Lista ordenada de menor a mayor:")
		mostrar_lista(lista)
# Funcion para mostrar el menu
def mostrar_menu():
	print("\n================================")
	print(" MENU - MANEJO DE LISTAS")
	print("================================")
	print("1. Llenar lista")
	print("2. Mostrar lista")
	print("3. Ordenar lista con sort()")
	print("4. Salir")
	print("================================")
# Funcion principal
def main():
	numeros = []
	while True:
		mostrar_menu()
		opcion = input("Seleccione una opcion (1-4): ").strip()
		if opcion == "1":
			llenar_lista(numeros)
		elif opcion == "2":
			mostrar_lista(numeros)
		elif opcion == "3":
			ordenar_lista(numeros)
		elif opcion == "4":
			print("\nGracias por utilizar el programa.")
			print("Fin del programa.")
			break
		else:
			print("Error: seleccione una opcion del 1 al 4.")
# Punto de entrada del programa
if __name__ == "__main__":
	main()