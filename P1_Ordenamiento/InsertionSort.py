#InsertionSort.py

def insertion_Sort(A):
# De un conjunto de enteros desordenados, se comparan los valores y sólo se
# intercambian de posición para su ordenación mientras se van desplazando.
    j = 1
    n = len(A)
    for j in range(n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i+1] = key
