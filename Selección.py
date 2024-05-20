def ord_seleccion(arreglo):
    n = len(arreglo)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]

arreglo = [6, 3, 1, 12, 0]
ord_seleccion(arreglo)

print(arreglo)
