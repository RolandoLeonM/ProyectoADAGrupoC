from HybridQuickSort import hybrid_quick_sort
from HeapSort import heapSort

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



# Driver code

a = [ 24, 97, 40, 67, 88, 85, 15,
	66, 53, 44, 26, 48, 16, 52,
	45, 23, 90, 18, 49, 80, 23 ]
hybrid_quick_sort(a, 0, 20)
print(a)
