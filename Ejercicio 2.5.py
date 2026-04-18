import time
import random
import matplotlib.pyplot as plt

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


def merge_sort(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    medio = len(arreglo) // 2

    izquierda = merge_sort(arreglo[:medio])
    derecha = merge_sort(arreglo[medio:])

    return merge(izquierda, derecha)


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr

def medir_tiempos():
    tamanos = [10, 50, 100, 500, 1000, 5000]

    tiempos_insertion = []
    tiempos_merge = []

    print(f"{'n':<10}{'Insertion Sort (s)':<20}{'Merge Sort (s)'}")

    for n in tamanos:
        arr = list(range(n))
        random.shuffle(arr)

        arr1 = arr.copy()
        arr2 = arr.copy()

        # Insertion Sort
        inicio = time.time()
        insertion_sort(arr1)
        tiempo_insertion = time.time() - inicio

        # Merge Sort
        inicio = time.time()
        merge_sort(arr2)
        tiempo_merge = time.time() - inicio

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(f"{n:<10}{tiempo_insertion:<20.6f}{tiempo_merge:.6f}")

    return tamanos, tiempos_insertion, tiempos_merge


def graficar(tamanos, tiempos_insertion, tiempos_merge):
    plt.figure()

    plt.plot(tamanos, tiempos_insertion, marker='o', label='Insertion Sort')
    plt.plot(tamanos, tiempos_merge, marker='o', label='Merge Sort')

    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación: Merge Sort vs Insertion Sort')
    plt.legend()
    plt.grid()
    plt.savefig("comparacion_insertion_vs_merge.png")

    plt.show()

if __name__ == "__main__":
    tamanos, tiempos_insertion, tiempos_merge = medir_tiempos()
    graficar(tamanos, tiempos_insertion, tiempos_merge)