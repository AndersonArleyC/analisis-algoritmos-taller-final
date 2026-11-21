# Taller final — parte de Anderson

Curso: Análisis de algoritmos · ITM · 2026-2

## Autoría

| Integrante | Usuario de Git | Ejercicios |
| --- | --- | --- |
| Anderson | `AndersonArleyC` | 215, 179, 743, 1584 |

> Antes de entregar, combine este contenido con el `README.md` general del grupo y agregue los demás integrantes.

## 1. [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Autor: Anderson (`AndersonArleyC`)  
Familia: heap  

**Idea.** Se mantiene un min-heap con los `k` valores más grandes encontrados. Cuando el heap supera el tamaño `k`, se elimina su mínimo. Al finalizar, la raíz es el k-ésimo mayor, pues es el menor elemento entre los `k` mayores.

**Complejidad.** Para `n = len(nums)`, tiempo `O(n log k)` y espacio extra `O(k)`.

Código: [`kth-largest/solution.py`](kth-largest/solution.py)  
Evidencia pendiente: `evidencias/kth-largest-accepted.png`

## 2. [179. Largest Number](https://leetcode.com/problems/largest-number/)

Autor: Anderson (`AndersonArleyC`)  
Familia: ordenamiento con comparador personalizado  

**Idea.** Los números se convierten a cadenas. Para dos cadenas `a` y `b`, `a` debe aparecer primero cuando `a + b > b + a`. Después de ordenar con esa regla, se concatenan las cadenas. Si el primer elemento es `"0"`, todos los números son cero y se devuelve `"0"`.

**Complejidad.** Para `n` números y longitud máxima `d`, el ordenamiento realiza `O(n log n)` comparaciones de costo `O(d)`: tiempo `O(d n log n)`. El espacio para las cadenas y el resultado es `O(nd)`; el sort de Python puede requerir además `O(n)` referencias auxiliares.

Código: [`largest-number/solution.py`](largest-number/solution.py)  
Evidencia pendiente: `evidencias/largest-number-accepted.png`

## 3. [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Autor: Anderson (`AndersonArleyC`)  
Familia: grafos — Dijkstra  

**Modelo.** Cada dispositivo es un vértice y cada registro `[u, v, w]` es un arco dirigido de `u` a `v` con peso no negativo `w`.

**Idea.** Se ejecuta Dijkstra desde `k` usando un min-heap de pares `(distancia, nodo)`. Cuando se extrae por primera vez un nodo no procesado, su distancia es definitiva. Si se alcanzan todos los nodos, la mayor distancia definitiva es el tiempo en que todos recibieron la señal; si falta alguno, se devuelve `-1`.

**Complejidad.** Con `n` vértices y `m = len(times)` arcos, tiempo `O((n + m) log n)` y espacio `O(n + m)`.

Código: [`network-delay-time/solution.py`](network-delay-time/solution.py)  
Evidencia pendiente: `evidencias/network-delay-time-accepted.png`

## 4. [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Autor: Anderson (`AndersonArleyC`)  
Familia: grafos — árbol de recubrimiento mínimo (Prim)

**Modelo.** Cada punto es un vértice de un grafo completo no dirigido. El peso entre dos puntos es su distancia de Manhattan.

**Idea.** Se usa Prim sin construir las `Theta(n^2)` aristas. En cada iteración se agrega al árbol el punto externo de menor costo conocido y se actualiza el costo de conectar los puntos restantes. La suma de las aristas elegidas es el costo del MST.

**Complejidad.** Para `n = len(points)`, tiempo `O(n^2)` y espacio extra `O(n)`.

Código: [`min-cost-to-connect-all-points/solution.py`](min-cost-to-connect-all-points/solution.py)  
Evidencia pendiente: `evidencias/min-cost-to-connect-all-points-accepted.png`

## Evidencias pendientes

Después de ejecutar **Submit** en LeetCode, guarde en `evidencias/` una captura por problema. Cada captura debe mostrar el número o título, `Accepted`, todos los casos en `Passed`, runtime/memoria cuando aparezcan y el usuario de LeetCode de Anderson.


