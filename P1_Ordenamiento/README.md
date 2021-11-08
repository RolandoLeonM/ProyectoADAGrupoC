<p></p>

<h1 align="center">Proyecto 01: Algoritmos de Ordenamiento</h1>

---

<div align="center">
  <strong>Universidad Nacional de San Agustín</strong><br>
  Facultad de Ingeniería de Producción y Servicios<br>
  <sub>Escuela Profesional de Ingeniería de Sistema</sub>
</div>

<br>

<div align="center">
    <span>Asignatura: Análisis y Diseño de Algoritmos - Segundo Semestre 2021-B</span>
    <span>Grupo: C</span>
</div>

<div align="center">
  <sub>Este trabajo fue elaborado con ❤︎ por:
    <a href="">Rolando León Mamani</a>
  </sub>
</div>

<br />

---

<h2 align="center">Introducción</h2>

Para este Proyecto 01 se han usado los algoritmos de Insertion Sort, Quick Sort, Heap Sort y también un algoritmo híbrido que es la combinación de Insertion Sort y Quick Sort, así mismo, se determinó el tamaño de cambio entre dichos algoritmos y el método de particionamiento adecuado para el pivot. Posteriormente se hizo una comparación entre Heap Sort y el algoritmo hibrido, para determinar el tiempo de ordenamiento de ambos.

# Algoritmos de Ordenamiento

## Insert Sort

* **Descripción:**

La ordenación por inserción está implementada en un algoritmo de comparación. Este algoritmo segmenta la lista en partes ordenadas y no ordenadas, aquí se crea una sublista de elementos ordenados de nuestra lista dada, y seguimos agregando nuevos elementos y ordenándolos iterativamente [1,2].

* **Complejidad algorítmica:**

La mejor entrada de caso es una lista desordenada. En este caso, la ordenación por inserción tiene un tiempo de ejecución lineal, es decir, O (n). La entrada del peor de los casos más simple es una matriz ordenada en orden inverso, esto le da a la ordenación por inserción un tiempo de ejecución cuadrático, es decir, O (n^2).

## Quick Sort

* **Descripción:**

Este algoritmo de divide y vencerás es el algoritmo de ordenación más utilizado. La ordenación rápida de este algoritmo es muy eficaz, que se utiliza a menudo para grandes conjuntos de datos. La ordenación rápida se basa en la partición de la lista en listas más pequeñas (según el punto de pivote). Los elementos se organizan en función de si son más pequeños o más grandes que el pivote [1,2].

* **Complejidad algorítmica:**

El peor de los casos es cuando el elemento más pequeño o más grande siempre se selecciona como pivote, esto crearía particiones de tamaño n-1, provocando llamadas recursivas n-1 veces, la complejidad de tiempo del peor caso de ordenación rápida es O (n^2). Si bien la función de partition utiliza bucles while anidados, hace comparaciones en todos los elementos de la lista para realizar sus intercambios. Como tal, tiene una complejidad temporal de O (n). Por lo tanto, la complejidad de tiempo del mejor caso y tiempo medio es O (nlogn).

## Heap Sort

* **Descripción:**

Heap Sort es una técnica de ordenación basada en comparaciones está basada en la estructura de datos de heap binario. Un árbol binario completo es un árbol binario en el que cada nivel, excepto posiblemente el último, está completamente lleno, y todos los nodos están lo más a la izquierda posible. Un árbol binario donde el elemento más grande es el nodo raíz. Un heap binario es un árbol binario completo donde los elementos se almacenan en un especial orden de modo que el valor en un nodo padre sea mayor (o menor) que los valores en sus dos nodos hijos [1,3].

* **Complejidad algorítmica:**

La complejidad de tiempo de heapify es O (logn). La complejidad de tiempo de creación de la función BuildHeap () es O (n) y la complejidad de tiempo general de Heap Sort es O (nLogn).

Para el mejor, promedio y peor caso, siempre será O (nLogn) [11].

## Implantación de algoritmo hibrido: Quick Sort + Insertion Sort

* **Descripción:**

Se dice que un algoritmo híbrido es cuando se combina más de un algoritmo. En este caso el algoritmo híbrido se implementa con la combinación de Quick Sort y Insertion Sort. El Quick Sort es eficiente si el tamaño de la entrada es muy grande. Pero, la ordenación por Insertion es más eficiente que la Quick Sort en el caso de arreglos pequeños, ya que el número de comparaciones e intercambios es menor en comparación con la de Quick Sort.

La idea es utilizar la recursividad y encontrar continuamente el tamaño de la matriz. Si el tamaño es mayor que el valor de umbral (10), entonces se llama a la función de Quick Sort para esa parte del arreglo. De lo contrario, se llama a Insertion Sort. Entonces combinamos los dos algoritmos para ordenar de manera eficiente usando ambos enfoques [4].

En la siguiente imagen se muestra como se realiza el ordenamiento:

![](images/hybridgfg.png?raw=true)
 <center><sub>Figura 01: Quick Sort + Insertion Sort [4]</sub></sub></center>

* **Selección de tamaño:**

La experimentación con un programa que registre tiempos de ejecución (profiler) es una buena forma de determinar el punto de ruptura. Una regla razonable es que a menos que n sea aproximadamente 100, puede ser una pérdida de tiempo implantar un algoritmo como Insert Sort [5].
El algoritmo de Insertion Sort también se puede utilizar para combinar con Quick Sort. Aunque la complejidad del tiempo es de O (N^2), estos algoritmos demuestran ser eficientes en este caso porque se usan solo cuando el tamaño del arreglo es menor que un valor de umbral que es 10, esto se toma en cuenta en la implementación [4].

Porque el tiempo de ejecución real (en segundos) del código real en una computadora real depende de qué tan rápido esa computadora ejecuta las instrucciones y qué tan rápido recupera los datos relevantes de la memoria, qué tan bien los almacena en caché, etc. La ordenación por inserción y la ordenación rápida utilizan diferentes instrucciones y tienen diferentes patrones de acceso a la memoria. Por lo tanto, el tiempo de ejecución de la ordenación rápida frente a la ordenación por inserción para cualquier conjunto de datos en particular en cualquier sistema en particular dependerá tanto de las instrucciones utilizadas para implementar esas dos rutinas de ordenación como de los patrones de acceso a la memoria de los datos. Dadas las diferentes combinaciones de instrucciones, es perfectamente posible que la ordenación por inserción sea más rápida para listas de hasta diez elementos en un sistema, pero solo para listas de hasta seis elementos en otro sistema [6].

La primera prueba fue la velocidad de ordenación por inserción frente a la velocidad de la ordenación rápida. Como se muestra en la Figura 2, Insertion Sort versus Quick Sort, los tiempos de ordenación se devolvieron como se esperaba: inicialmente el algoritmo Insert Sort funcionó mejor que Quick Sort. Luego, en un umbral particular en algún lugar entre 10 y 90, Quick Sort se volvió más eficiente. Notamos que esta región variaba bastante dependiendo de diferentes características de la computadora, lo más importante la velocidad del procesador, por lo que ejecutamos estas pruebas utilizando varias velocidades de procesador diferentes [12].

![](images/InsertionVsQuick.png?raw=true)
 <center><sub>Figura 02: Insertion Sort vs. Quick Sort [12]</sub></center>

En pruebas de más de 100, vemos una tendencia en la que Quick Sort comenzó a funcionar mucho mejor que un tipo de Insertion Sort. Esto era de esperar debido al análisis asintótico de los tipos; El Insertion Sort es O (n) y Quick Sort es O (n Ig n), por lo que esperábamos que esta tendencia se indicara en nuestros datos. Nosotros también señaló que ambos algoritmos no se ocuparían de tamaños de muestra de 100.000 o más, específicamente en predatos ordenados, debido a errores de desbordamiento de pila. Esto fue, en muchos aspectos, un déficit de hardware [12].

> Por lo tanto, para el tamaño de cambio entre Insert Sort y Qick Sort, es un tamaño menor a 10 elementos.

* **El método para la función de partición:**

Hay dos algoritmos populares para dividir un arreglo. Los esquemas de partición de Lamuto y Hoare, ordenan con éxito el arreglo dado, aunque el esquema de Hoare generalmente se considera más eficiente. El esquema de Lamuto ejecuta 3 veces más intercambios que el esquema de Hoare en promedio. El esquema de Hoare gana cuando la matriz contiene muchos elementos repetidos, ya que el de Lamuto intercambia repetidamente elementos repetidos innecesariamente [7].

Desde una dimensión pedagógica, Debido a su simplicidad, el método de partición de Lomuto podría ser más fácil de implementar (Introduction to algorithms - Thomas H. Cormen, lo sugiere en su libro). Pero vista desde una dimensión de rendimiento, para un uso práctico, la facilidad de implementación podría ser sacrificada en aras de la eficiencia. Sobre una base teórica, podemos determinar el número de comparaciones de elementos y swaps para comparar el rendimiento. Además, el tiempo real de ejecución estará influenciado por otros factores, como el rendimiento del almacenamiento en caché y las predicciones erróneas de las ramas. Entonces, los algoritmos se comportan de manera muy similar en permutaciones aleatorias, excepto por el número de intercambios. ¡Allí Lomuto necesita tres veces más que Hoare! [8,9,10].

> Para la implementación del algoritmo híbrido de Qick Sort, se utilizó el esquema de Haore.

* **Comparación entre Heap Sort y algoritmo hibrido de Qick Sort:**

Para la comparación en cuanto el tiempo que tardan en ordenamiento de datos, se muestra en la figura 3, Hybrid Quick Sort versus Heap Sort.

![](images/hqsVShp.png?raw=true)
 <center><sub>Figura 03: Hybrid Quick Sort versus Heap Sort (Elaboración propia)</sub></center>

Podemos observar que en umbral de 10 funcionan igual ambos, pero a partir de este punto Hybrid Quick Sort funciona mucho mejor que Heap Sort hasta el umbral 50, en donde Heap Sort va mejorando hasta el umbral 85, presentando luego un pico hasta un umbral 110 y a partir de ahí estos van tomando distancias paralelas.

> Por lo tanto, el algoritmo de Hybrid Quick Sort es más eficiente que Heap Sort.


## Conclusiones

* Los algoritmos de ordenación son eficientes con cierto número de datos, también depende de otras variables propias de hardware.

* Los algoritmos híbridos que se implementan con Quick Sort son mucho más eficientes frente a otros que no lo son.

* Los algoritmos de ordenamiento deben usarse dependiendo del tamaño de datos que se van a procesar, así también tener en cuenta las características de hardware, aunque esto no influye mucho al momento de hallar la complejidad computacional.



## Referencias

[1] [Algoritmos de ordenación en Python](https://pharos.sh/algoritmos-de-ordenacion-en-python/)

[2] [Sorting Algorithms in Python](https://dev.to/siddhartha280601/sorting-algorithms-in-python-33mm)

[3] [Heapsort](https://www.geeksforgeeks.org/heap-sort/)

[4] [Advanced Quick Sort (Hybrid Algorithm)](https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/)

[5] [Libro Estructura de Datos y Algoritmos de Alfred V. Aho y otros (Pág 259: Limitaciones de los algoritmos simples)](https://www.academia.edu/23710587/Estructura_de_Datos_y_Algoritmos_Aho_Hopcroft_Ullman)

[6] [Why is the optimal cut-off for switching from Quicksort to Insertion sort machine dependent?](https://cs.stackexchange.com/questions/37956/why-is-the-optimal-cut-off-for-switching-from-quicksort-to-insertion-sort-machin)

[7] [Introducción a los algoritmos: comprensión de QuickSort](https://ichi.pro/es/introduccion-a-los-algoritmos-comprension-de-quicksort-94708718133784)

[8] [Particionamiento Quicksort: Hoare vs. Lomuto](https://qastack.mx/cs/11458/quicksort-partitioning-hoare-vs-lomuto)

[9] [Quicksort (Quicksort)](https://programmerclick.com/article/2326629088/)

[10] [Ordenación rápida](https://www.it-swarm-es.com/es/algorithm/comprender-la-clasificacion-rapida/828500891/)

[11] [Heap sort algorithm](https://dev.to/ayabouchiha/heap-sort-algorithm-247h)

[12] [Speeds of Insertion and Quick Sort](https://www.alexlaird.com/content/uploads/2009/12/speedsofinsertionandquicksort.pdf)

