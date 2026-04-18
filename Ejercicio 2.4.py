import time
import random
import matplotlib.pyplot as plt

def max_subarray_bruteforce(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

def max_crossing_subarray(arr, low, mid, high):
    left_sum = float("-inf")
    suma = 0

    for i in range(mid, low - 1, -1):
        suma += arr[i]
        left_sum = max(left_sum, suma)

    right_sum = float("-inf")
    suma = 0

    for j in range(mid + 1, high + 1):
        suma += arr[j]
        right_sum = max(right_sum, suma)

    return left_sum + right_sum


def max_subarray(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left = max_subarray(arr, low, mid)
    right = max_subarray(arr, mid + 1, high)
    cross = max_crossing_subarray(arr, low, mid, high)

    return max(left, right, cross)

def obtener_datos():
    tamanos = [10, 50, 100, 200, 500, 1000]
    tiempos_fb = []
    tiempos_dv = []

    for n in tamanos:
        arr = [random.randint(-10, 10) for _ in range(n)]

        # Fuerza bruta
        inicio = time.time()
        max_subarray_bruteforce(arr)
        tiempos_fb.append(time.time() - inicio)

        # Divide y vencerás
        inicio = time.time()
        max_subarray(arr, 0, len(arr) - 1)
        tiempos_dv.append(time.time() - inicio)

    return tamanos, tiempos_fb, tiempos_dv

def graficar():
    tamanos, tiempos_fb, tiempos_dv = obtener_datos()

    plt.figure()
    plt.plot(tamanos, tiempos_fb, marker='o', label='Fuerza Bruta')
    plt.plot(tamanos, tiempos_dv, marker='o', label='Divide y Vencerás')

    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de algoritmos de subarreglo máximo')
    plt.legend()
    plt.grid()
    plt.savefig("comparacion_brute_force_vs_divide_and_conquer.png")

    plt.show()


if __name__ == "__main__":
    graficar()