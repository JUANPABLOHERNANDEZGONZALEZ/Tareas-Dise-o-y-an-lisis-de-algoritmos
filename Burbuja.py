def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1): 
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

arreglo = [6, 3, 1, 12, 0]
ord_burbuja(arreglo)

print(arreglo)