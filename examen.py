def generar(n):
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    fila_inicial = 0
    fila_final = n - 1
    columna_inicial = 0
    columna_final = n - 1

    while fila_inicial <= fila_final and columna_inicial <= columna_final:
        # Llenar fila superior
        for i in range(columna_inicial, columna_final + 1):
            matriz[fila_inicial][i] = valor
            valor += 1
        fila_inicial += 1

        # Llenar columna derecha
        for i in range(fila_inicial, fila_final + 1):
            matriz[i][columna_final] = valor
            valor += 1
        columna_final -= 1

        # Llenar fila inferior
        for i in range(columna_final, columna_inicial - 1, -1):
            matriz[fila_final][i] = valor
            valor += 1
        fila_final -= 1

        # Llenar columna izquierda
        for i in range(fila_final, fila_inicial - 1, -1):
            matriz[i][columna_inicial] = valor
            valor += 1
        columna_inicial += 1

    return matriz

def imprimir(matriz):
    for fila in matriz:
        print(fila)

# Solicitar al usuario el tamaño de la matriz
tamano = int(input("Cual es el tamaño de la matriz: "))
matriz = generar(tamano)
imprimir(matriz)
