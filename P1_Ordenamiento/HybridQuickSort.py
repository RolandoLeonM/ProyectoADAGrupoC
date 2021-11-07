from InsertionSort import insertion_sort

# HybridQuickSort.py

# Partición del método de Hoare
# Tony Hoare es el creador del algoritmo de Quick Sort.
def partition(arr, low, high):
# Dado un conjunto de valores, la posicion inicial y final
# del arreglo la funcion nos retornara el indice de partición.
# Se devuelve para que los subarreglos restantes puedan ordenarse
# de forma recursiva.

    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Si un elemento en i (a la izquierda del pivote)
        # es más grande que el elemento en j (a la derecha
        # del pivote), luego los intercambia
        arr[i], arr[j] = arr[j], arr[i]


# # Partición del método de Lotumo
# # es menos eficiente
# def partition(arr, low, high):
#
# 	pivot = arr[high]
# 	i = j = low
# 	for i in range(low, high):
# 		if arr[i] < pivot:
# 			arr[i], arr[j] = arr[j], arr[i]
# 			j += 1
# 	arr[j], arr[high] = arr[high], arr[j]
# 	return j

def quick_sort(arr, low, high):
# Dado un conjunto de valores y posiciones inicial
# y final del arreglo, la funcion llama a la funcion
# de particion y realiza un ordenamieno rápido de
# forma recursiva, retorna el array ordenado.

	if low < high:
		pivot = partition(arr, low, high)
		quick_sort(arr, low, pivot - 1)
		quick_sort(arr, pivot + 1, high)
		return arr

# Hybrid function -> Quick sort + Insertion sort
def hybrid_quick_sort(arr, low, high):
# Dado un conjunto de valores y posiciones inicial
# y final del arreglo, la función realiza ordenamiento
# recursivo mediante particiones en subarreglos y llama
# a la función insertion sort cuando el tamaño del
# subarreglo es menor a 10.

	while low < high:

		if high - low + 1 < 10:
            # Si el tamaño del arreglo es menor
            # que 10 aplica la ordenación por inserción
            # y detiene la recursividad
			insertion_sort(arr, low, high)
			break

		else:
			pivot = partition(arr, low, high)

			# Ordenamiento rapido optimizado que funciona en
            # los arreglos más pequeños primero

			if pivot - low < high - pivot:
                # Si el lado izquierdo del pivote es menor que
                # la derecha, ordena la parte izquierda
                # y mueve a la parte derecha del arreglo
				hybrid_quick_sort(arr, low, pivot - 1)
				low = pivot + 1
			else:
                # Si el lado derecho del pivote es menor
                # que a la izquierda, ordena el lado derecho y
                # mover hacia el lado izquierdo
				hybrid_quick_sort(arr, pivot + 1, high)
				high = pivot - 1
