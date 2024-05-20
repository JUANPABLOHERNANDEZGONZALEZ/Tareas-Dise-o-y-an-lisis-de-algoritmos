def quicksort(arreglo, low, high):
    if low < high:
        pi = partir(arreglo, low, high)
        quicksort(arreglo, low, pi - 1)
        quicksort(arreglo, pi + 1, high)

def partir(arreglo, low, high):
    pivot = arreglo[high]
    i = low - 1
    for j in range(low, high):
        if arreglo[j] < pivot:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    arreglo[i + 1], arreglo[high] = arreglo[high], arreglo[i + 1]
    return i + 1

arreglo = [6, 3, 1, 12, 0]
quicksort(arreglo, 0, len(arreglo) - 1)

print(arreglo)
