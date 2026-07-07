# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:53:52 2026

@author: Darky485
"""

"""
Al casino de Rajshahi han tingut una nit molt animada. Els jugadors van fent apostes i el gerent vol saber quin ha estat el guany més gran de la nit per donar-li un premi especial a aquell jugador afortunat.

Entrada
L'entrada consta d'una seqüència de números enters que representen els guanys de cada aposta (poden ser negatius si han perdut). La seqüència acaba amb un 0 que no s'ha de processar.

Sortida
Mostra el guany més gran de la nit.

Exemple d'Entrada
150
-50
200
-30
75
-100
25
0

Exemple de Sortida
200
"""

ganancia_mayor = 0
entrada = int(input())

while entrada != 0:
    if entrada > ganancia_mayor:
        ganancia_mayor = entrada
    
    entrada = int(input())

print(ganancia_mayor)