def merge_sort(arreglo):
    if len(arreglo) > 1:
        mid = len(arreglo) // 2
        left_half = arreglo[:mid]
        right_half = arreglo[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arreglo[k] = left_half[i]
                i += 1
            else:
                arreglo[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arreglo[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arreglo[k] = right_half[j]
            j += 1
            k += 1

arreglo = [6, 3, 1, 12, 0]
merge_sort(arreglo)

print(arreglo)
