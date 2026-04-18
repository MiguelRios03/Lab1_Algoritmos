# EJERCICIOS MANUALES

## Ejercicio 1: Solución manual del problema del subarreglo máximo

Aplicar manualmente el algoritmo divide y vencerás sobre el arreglo construido.  

El procedimiento debe incluir:  

* División recursiva del arreglo  
* Cálculo del subarreglo máximo en la mitad izquierda  
* Cálculo del subarreglo máximo en la mitad derecha  
* Cálculo del subarreglo máximo cruzado  
* Comparación final de los tres casos  
* Identificación del subarreglo máximo resultante  

Se recomienda representar el procedimiento mediante diagramas tipo  ́arbol, como los vistos en clase.  

### Arreglo utilizado

[1, -3, 3, -1, 5, -3, 3, -5, 6, -3]  

### División del arreglo

Se divide el arreglo en dos mitades:  

Izquierda: [1, -3, 3, -1, 5]  
Derecha: [-3, 3, -5, 6, -3]  

### Caso izquierdo

Con la parte izquierda  
[1, -3, 3, -1, 5]  

Dividimos la primera vez  
[1, -3 ] | [3, -1, 5]  

Teniendo la subdivisión 1  
[1, -3]  

Dividimos nuevamente  
[1] | [-3]  

Y como ya tenemos subarreglos de 1 solo elemento no podemos dividir más, por lo tanto, comparamos y seleccionamos el mejor  
[1] -> 1  
[-3] -> -3  
[1, -3] -> -2  

El mejor subarreglo de la subdivisión 1 es  
[1]  

Ahora con el resto de la mitad izquierda, la subdivision 2:  
[3, -1, 5]  

Dividimos  
[3] | [-1, 5]  
[3] -> 3  

Ahora con  
[-1, 5]  

Seguimos dividiendo  
[-1] | [5]  

Comparamos la primera parte de la subdivisión 2  
[-1] -> -1  
[5] -> 5  
[-1, 5] -> 4  

Como el mejor subarreglo de esta primera parte de la subdivisión 2 es [5], lo comparamos con los subarreglos de la segunda parte de la subdivisión 2 y con el subarreglo de la subdivisión 2  

[3] -> 3  
[5] -> 5  
[3, -1, 5] -> 7  


El mejor subarreglo de la mitad izquierda es  
[3, -1, 5]  

Con suma: 7  

--- 

### Caso derecho
Con la parte derecha  
[-3, 3, -5, 6, -3]  

Dividimos la primera vez  
[-3, 3] | [-5, 6, -3]  

Teniendo la subdivisión 1  
[-3, 3]  

Dividimos nuevamente  
[-3] | [3]  

Y como ya tenemos subarreglos de 1 solo elemento no podemos dividir más, por lo tanto, comparamos y seleccionamos el mejor  
[-3] -> -3  
[3] -> 3  
[-3, 3] -> 0  

El mejor subarreglo de la subdivisión 1 es  
[3]  

Ahora con el resto de la mitad derecha, la subdivision 2:  
[-5, 6, -3]  

Dividimos  
[-5] | [6, -3]  
[-5] -> -5  

Ahora con  
[6, -3]  

Seguimos dividiendo  
[6] | [-3]  

Comparamos la primera parte de la subdivisión 2  
[6] -> 6  
[-3] -> -3  
[6, -3] -> 3  


Como el mejor subarreglo de esta primera parte de la subdivisión 2 es [6], lo comparamos con los subarreglos de la segunda parte de la subdivisión 2 y con el subarreglo de la subdivisión 2  

[-5] -> -5  
[6] -> 6  
[-5, 6, -3] -> -2  

El mejor subarreglo de la mitad derecha es  
[6]  

Con suma: 6  

---

### Caso cruzado
Arreglo completo  
[1, -3, 3, -1, 5 | -3, 3, -5, 6, -3]  

Desde el centro hacía la izquierda  
[5] → 5  
[-1, 5] → 4  
[3, -1, 5] → 7  
[-3, 3, -1, 5] → 4  
[1, -3, 3, -1, 5] → 5  

Mejor resultado:  
[3, -1, 5]  

con suma: 7  

Desde el centro hacia la derecha:  

[-3] → -3  
[-3, 3] → 0  
[-3, 3, -5] → -5  
[-3, 3, -5, 6] → 1  
[-3, 3, -5, 6, -3] → -2  

Mejor resultado:  
[-3, 3, -5, 6]  

con suma: 1  

Sumamos ambos:  
7 + 1 = 8  

Entonces el subarreglo cruzado tiene suma: 8  

### Comparación final  
Izquierda → 5  
Derecha → 6  
Cruzado → 8  

### Resultado final  
El subarreglo máximo es:  
[3, -1, 5, -3, 3, -5, 6]  

Con suma máxima: 8  

## Ejercicio 2: Solución manual del algoritmo Merge Sort
Aplicar manualmente el algoritmo Merge Sort sobre el arreglo construido en la sección anterior.  

El procedimiento debe incluir:  

* Divisiones sucesivas del arreglo hasta alcanzar el caso base  
* Identificación del caso base  
* Proceso de mezcla paso a paso  
* Resultado final ordenado  

Se recomienda representar el procedimiento mediante diagramas tipo árbol, como los vistos en clase.  

### Arreglo utilizado

[1, 3, 3, 1, 5, 3, 3, 5, 6, 3]  

### División del arreglo

Dividimos el arreglo en dos partes:  

[1, 3, 3, 1, 5] | [3, 3, 5, 6, 3]  

Seguimos dividiendo:  

[1, 3] | [3, 1, 5]   --    [3, 3] | [5, 6, 3]  

Continuamos:

[1] | [3]     [3] | [1, 5]  --   [3] | [3]     [5] | [6, 3]  

Terminamos de dividir hasta llegar al caso base:  

[1] [3] [3] [1] [5] [3] [3] [5] [6] [3]  

### Caso base

Cada subarreglo de un solo elemento ya está ordenado por si mismo:  
[1], [3], [3], [1], [5], [3], [3], [5], [6], [3]  

### Proceso de mezcla
Vamos a combinar dos listas ordenadas en una sola lista ordenada.  
[1], [3] | [3], [1] | [5], [3] | [3], [5] | [6], [3]  

Ahora unimos las listas de 1 elemento, comparamos y ordenamos de menor a mayor dentro de cada una para al final unirlas en 1 lista de 2 elementos   
1 < 3    | 3 > 1    | 5 > 3    | 3 < 5    | 6 > 3            
[1, 3]   | [1, 3]   | [3, 5]   | [3, 5]   | [3, 6]  

Ahora unimos las listas de 2 elementos, comparamos y ordenamos de menor a mayor dentro de cada una para al final unirlas en 1 lista  
[1, 3], [1, 3] | [3, 5] | [3, 5], [3, 6]  

Obteniendo   
[1, 1, 3, 3] | [3, 5] | [3, 3, 5, 6]  

Ahora con   
[1, 1, 3, 3], [3, 5] | [3, 3, 5, 6]  

Seguimos unificando las listas ordenadas de menor a mayor  
[1, 1, 3, 3, 3, 5] | [3, 3, 5, 6]  

Y finalmente, reconstruimos el arreglo comparando de menor a mayor cada dato de ambas listas y unificandolas  
[1, 1, 3, 3, 3, 3, 3, 5, 5, 6]  

### Resultado final ordenado  
Obtuvimos  
[1, 1, 3, 3, 3, 3, 3, 5, 5, 6]  