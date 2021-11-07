# HeapSort.py

def heapify(arr, n, i):
# Dado un conjunto de valores, el numero total de elementos
# y la posición del último padre, la función va apilando el
# mayor de los elementos

	largest = i # Initialize largest as root (posicion ultimo padre - raiz)
	l = 2 * i + 1	 # left = 2*i + 1 (posicion hijo izquierdo)
	r = 2 * i + 2	 # right = 2*i + 2 (posicion hijo derecho)

    # Verifica si el hijo izquierdo de la raiz existe y es
    # mayor que la raiz
	if l < n and arr[largest] < arr[l]:
		largest = l

    # Verifica si el hijo derecho de la raiz existe y es
    # mayor que la raíz
	if r < n and arr[largest] < arr[r]:
		largest = r

    # Se cambia la raiz si es necesario
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap (intercambio)

		# Apila la raiz, mediante llamado recursivo
		heapify(arr, n, largest)


def heapSort(arr):
# Dado un conjunto de valores a función es la principal
# para ordenar los elementos dados

	n = len(arr) # tamano del array

	# Construye el maximo heap (BuildHeap).
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# Uno por uno se extraen los elementos
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap (intercambio)
		heapify(arr, i, 0)
