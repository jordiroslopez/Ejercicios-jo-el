# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:48:53 2026

@author: Darky485
"""

"""
A la ruleta del casino de Comilla hi ha números del 0 al 36. Alguns jugadors només aposten als números senars (imparells) perquè creuen que donen més sort. El crupi necessita un programa que mostri tots els números senars des de l'1 fins a un cert número per ajudar els jugadors a fer les seves apostes.

Entrada
Cada cas conté un número enter positiu N.

Sortida
Mostra tots els números imparells des de l'1 fins a N (inclòs si N és imparell).

Exemple d'Entrada
10

Exemple de Sortida
1
3
5
7
9
"""

n = int(input())

for numero in range(1, n+1):
    if numero % 2 != 0:
        print(numero)