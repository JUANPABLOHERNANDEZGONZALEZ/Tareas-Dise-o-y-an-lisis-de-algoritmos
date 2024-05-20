def heapify(arreglo, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arreglo[left] > arreglo[largest]:
        largest = left

    if right < n and arreglo[right] > arreglo[largest]:
        largest = right

    if largest != i:
        arreglo[i], arreglo[largest] = arreglo[largest], arreglo[i]
        heapify(arreglo, n, largest)

def heap_sort(arreglo):
    n = len(arreglo)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arreglo, n, i)

    for i in range(n - 1, 0, -1):
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
        heapify(arreglo, i, 0)

arreglo = [6, 3, 1, 12, 0]
heap_sort(arreglo)

print(arreglo)
