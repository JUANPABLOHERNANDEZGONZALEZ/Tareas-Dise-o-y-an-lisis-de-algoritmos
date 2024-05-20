def ord_insercion(arreglo):
    n = len(arreglo)

    for i in range(1, n):
        key = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j] > key:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = key

arreglo = [6, 3, 1, 12, 0]
ord_insercion(arreglo)

print(arreglo)
