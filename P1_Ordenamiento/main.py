import random
import time
from HybridQuickSort import hybrid_quick_sort
from HeapSort import heapSort

def generateValuesRandom(size):
# Genera lista de números aleatorios de acuerdo al tamaño dado,
# determinado con valor incial, valor final y salto o paso
    lista = [random.randint(1,1000) for i in range(size)]
    #lista = [random.randrange(0, 10_000, 10) for _ in range(size)]
    return lista

x = 100 # tamaño de datos

values = generateValuesRandom(x)
n = len(values) - 1
values1 = values
values2 = values

#print(values1)
timeIni = time.perf_counter()
hybrid_quick_sort(values1, 0, n)
timeFin = time.perf_counter()
#print(values1)
print(f"Tiempo transcurrido hybrid quick sort: {timeFin - timeIni:0.6f} segundos")

print("")

#print(values2)
timeIni = time.perf_counter()
heapSort(values2)
timeFin = time.perf_counter()
#print(values2)
print(f"Tiempo transcurrido heap sort: {timeFin - timeIni:0.6f} segundos")

















# values = [4, 5, 12, 45, 78, 15, 36,28, 11, 69]
# insertionSort(values)
# print(values)

# # Driver code
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
#
# print("Sorted array is")
# for i in range(n):
# 	print("%d" % arr[i]),
# # This code is contributed by Mohit Kumra


# # Driver code
#
# a = [ 24, 97, 40, 67, 88, 85, 15,
# 	66, 53, 44, 26, 48, 16, 52,
# 	45, 23, 90, 18, 49, 80, 23 ]
# hybrid_quick_sort(a, 0, 20)
# print(a)
