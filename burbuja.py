def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos del arreglo que sean mayores que key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Buscar el elemento mínimo restante
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Prueba de los tres métodos
original_list = [64, 34, 25, 12, 22, 11, 90]

# Copias para cada algoritmo
list_bubble = original_list.copy()
list_insertion = original_list.copy()
list_selection = original_list.copy()

bubble_sort(list_bubble)
insertion_sort(list_insertion)
selection_sort(list_selection)

print("Original:", original_list)
print("Ordenado con Burbuja:  ", list_bubble)
print("Ordenado con Inserción:", list_insertion)
print("Ordenado con Selección:", list_selection)
