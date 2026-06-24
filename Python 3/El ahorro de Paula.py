# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:39:20 2026

@author: Darky485
"""

"""
Paula quiere comprarse una consola que cuesta C euros. Ella recibe una paga semanal de P euros y cada semana puede decidir si ahorrar todo o gastárselo en caprichos.

Paula tiene una regla: ahorra toda su paga únicamente las semanas impares (semana 1, 3, 5, …). Las semanas pares se lo gasta todo. Además, si en algún momento ya tiene suficiente dinero para comprar la consola, deja de ahorrar inmediatamente.

Dado el precio de la consola, la paga semanal y el número de semanas N, ¿cuánto dinero tendrá Paula al final de las N semanas?

Entrada
La primera línea indica el número de casos de prueba. Cada caso de prueba contiene tres enteros C, P, N (1 ≤ C ≤ 1000, 1 ≤ P ≤ 100, 1 ≤ N ≤ 100), el precio de la consola, la paga semanal, y el número de semanas.

Salida
Para cada caso, muestra el dinero que tendrá Paula al final de las N semanas. En el caso que los valores estén fuera de rango, se mostrarà el primer valor.

Ejemplo d'Entrada
Copy
3
50 10 10
100 25 3
30 20 2
Ejemplo de Salida
Copy
50
50
20
Explicación de los tests

Primer test: Semanas 1,3,5,7,9 ahorra 10€. En semana 5 ya tiene 50€, así que para. Total = 50€.
Segundo test: Semana 1 ahorra 25€, semana 2 gasta, semana 3 ahorra 25€. Total = 50€.
Tercer test: Semana 1 ahorra 20€, semana 2 gasta. Total = 20€.
"""

ciclos = int(input())

for i in range(ciclos):
    entrada = input().split()
    c = int(entrada[0])
    p = int(entrada[1])
    n = int(entrada[2])
    ahorro = 0
    
    for j in range(1, n+1, 1):
        if j % 2 != 0:
            ahorro += p
        if ahorro >= c:
            ahorro = c
            break
        
    print(ahorro)
