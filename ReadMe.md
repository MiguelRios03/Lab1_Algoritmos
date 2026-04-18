# Laboratorio #1 - Algoritmos (Recursividad, Divide y Vencerás, Merge Sort)

## INFORMACIÓN GENERAL

**Presentado por:** Miguel Angel Rios Ochoa  
**Materia:** Analisis de algoritmos  
**Código clase:** 190304006-1  
**Profesor:** SANTIAGO SUAREZ CORTES  
**Universidad:**Instituto tecnológico metropolitano (I.T.M)  
**Facultad:** Ingenierías  
**Tema:** Recursividad, Divide y Vencerás, Merge Sort  
**Fecha limite:** 18-04-2026  

---

## INTRODUCCIÓN

En este laboratorio evidenciaremos con claridad que la recursividad y el paradigma de divide y vencerás son unos conceptos fundamentales para el análisis y el diseño de algoritmos. La recursividad consiste en la capacidad de que un algoritmo pueda llamarse a sí mismo para resolver un problema, descomponiendose en instancias mucho más pequeñas hasta alcanzar un caso base para detener el proceso, teniendo en cuenta que este caso base debe ser definido con cuidado ya que sin este se causan bucles infinitos.

Por otro lado, el paradigma de divide y vencerás se basa en dividir un problema muy complejo en subproblemas mucho más simples del mismo tipo. Esto para resolverlos de manera independiente y luego combinar sus soluciones para obtener el resultado final. Este enfoque es ampliamente utilizado en los algoritmos más eficientes; como los de ordenamiento y búsqueda.

Por lo tanto, podemos decir con certeza que ambos conceptos son esenciales porque permiten el desarrollo de soluciones más claras, estructuradas y, en la mayoria de los casos, más eficientes, facilitando la resolución de problemas complejos.

---

## PREGUNTAS

### 1. La recursividad es:
a) Un algoritmo iterativo  
b) Un algoritmo que usa  ́unicamente ciclos  
c) Un algoritmo que se llama a sí mismo  
d) Un algoritmo que no tiene caso base  

### 2. El caso base en un algoritmo recursivo permite:
a) Aumentar la complejidad del algoritmo  
b) Detener la ejecución de la recursión  
c) Duplicar las llamadas recursivas  
d) Eliminar estructuras iterativas  

### 3. ¿Cuál es una desventaja de la recursividad?
a) No puede expresar problemas matemáticos  
b) Puede consumir más memoria  
c) Siempre es más rápida que un ciclo  
d) No puede retornar valores  

### 4. El paradigma divide y vencerás consiste en:
a) Resolver el problema utilizando ciclos anidados  
b) Dividir el problema en subproblemas más pequeños, resolverlos y combinar sus soluciones  
c) Ordenar los datos antes de procesarlos  
d) Aplicar programación dinámica  

### 5. En el problema del máximo subarreglo, ¿cuántos casos posibles existen al dividir el arreglo mediante el paradigma divide y vencerás? Enuncie cada caso
a) 2  
b) 3  
c) 4  
d) 5  

### 6. En Merge Sort y el problema del máximo subarreglo, ¿Cuál es el caso base de los algoritmos?
a) Cuando el arreglo tiene dos elementos  
b) Cuando el arreglo tiene un elemento  
c) Cuando el arreglo tiene un negativo  
d) Cuando el arreglo es positivo  

### 7. La complejidad temporal del algoritmo Merge Sort es:
a) O(n)  
b) O(n^2)  
c) O(n log n)  
d) O(log n)  

### 8. El problema del subarreglo máximo busca:
a) El elemento más grande del arreglo  
b) El subarreglo con mayor número de elementos  
c) El subarreglo contiguo cuya suma es máxima  
d) El promedio m ́as alto del arreglo  

### 9. El algoritmo Insertion Sort pertenece a la categoría de algoritmos:
a) Divide y vencerás  
b) Iterativos con complejidad cuadrática  
c) Logarítmicos  
d) Recursivos puros  

### 10. En el paradigma divide y vencerás, el problema original se resuelve:
a) Eliminando subproblemas innecesarios  
b) Transformándolo en subproblemas más pequeños del mismo tipo  
c) Ordenando previamente los datos  
d) Aplicando programación dinámica  

## RESPUESTAS

### 1. La recursividad es:
c) Un algoritmo que se llama a sí mismo

### 2. El caso base en un algoritmo recursivo permite:
b) Detener la ejecución de la recursión

### 3. ¿Cuál es una desventaja de la recursividad?
b) Puede consumir más memoria

### 4. El paradigma divide y vencerás consiste en:
b) Dividir el problema en subproblemas más pequeños, resolverlos y combinar sus soluciones

### 5. En el problema del máximo subarreglo, ¿cuántos casos posibles existen al dividir el arreglo mediante el paradigma divide y vencerás? Enuncie cada caso
b) 3 
CASOS:
    Completamente en la mitad izquierda 
    Completamente en la mitad derecha 
    Cruzando el punto medio.

### 6. En Merge Sort y el problema del máximo subarreglo, ¿Cuál es el caso base de los algoritmos?
b) Cuando el arreglo tiene un elemento

### 7. La complejidad temporal del algoritmo Merge Sort es:
c) O(n log n)

### 8. El problema del subarreglo máximo busca:
c) El subarreglo contiguo cuya suma es máxima

### 9. El algoritmo Insertion Sort pertenece a la categoría de algoritmos:
b) Iterativos con complejidad cuadrática

### 10. En el paradigma divide y vencerás, el problema original se resuelve:
b) Transformándolo en subproblemas más pequeños del mismo tipo

---
