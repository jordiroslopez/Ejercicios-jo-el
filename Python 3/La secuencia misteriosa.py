# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:01:10 2026

@author: Darky485
"""

"""
Una secuencia tiene una propiedad especial: es casi creciente si podemos eliminar como máximo un elemento y conseguir que la secuencia resultante sea estrictamente creciente.

Por ejemplo:
• [1, 3, 2, 4] es casi creciente (podemos eliminar el 3 o el 2).
• [1, 2, 3, 4] es casi creciente (ya es creciente, no hace falta eliminar nada).
• [4, 3, 2, 1] NO es casi creciente.
• [1, 2, 1, 2] NO es casi creciente (haría falta eliminar más de un elemento).

Dada una secuencia de N números, determina si es casi creciente o no.

Entrada
La primera línea indica el número de casos de prueba. Cada caso de prueba empieza con un entero N (2 ≤ N ≤ 100), el número de elementos. La siguiente línea contiene N enteros Ai (1 ≤ Ai ≤ 1000), los elementos de la secuencia.

Salida
Para cada caso, muestra SI si la secuencia es casi creciente, o NO en caso contrario.

Ejemplo de Entrada
5
4
1 3 2 4
5
1 2 3 4 5
4
4 3 2 1
5
1 2 1 2 3
6
1 2 5 3 4 6

Ejemplo de Salida:
SI
SI
NO
NO
SI
Explicación del caso:

• Caso 1: Eliminando el 3 → [1,2,4] es creciente.
• Caso 2: Ya es creciente.
• Caso 3: Imposible conseguirlo eliminando solo un elemento.
• Caso 4: Habría que eliminar dos elementos.
• Caso 5: Eliminando el 5 → [1,2,3,4,6] es creciente.
"""

cdp = int(input())

for i in range(cdp):
    n = int(input())
    enteros = input().split()
    enteros = list(map(int, enteros))
    
    casi_creciente = False
    
    for j in range(1, n):
        aux_enteros = enteros.copy()
        aux = aux_enteros.pop(j)
        if all(x < y for x, y in zip(aux_enteros, aux_enteros[1:])):
            casi_creciente = True
            break
        
    if casi_creciente:
        print("SI")
    else:
        print("NO")
