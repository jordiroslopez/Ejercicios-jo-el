# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:37:11 2026

@author: Darky485
"""

"""
En 2019 la OCDE va fer un informe molt polèmic que deia que cobrar més de 30400 euros bruts a l'any a Espanya era ser de classe alta. Van haver-hi moltes protestes després d'aquest informe i encara avuí segueix sent font de memes

:(

Entrada
Cada cas és de una línea, i conté un número, el sou brut anual.

Sortida
Per cada cas es dira "SI" si el sou es igual o superior a 30400 euros bruts i "NO" en cas contrari

Exemples
Entrada	Sortida
30400	SI
30200	NO
30500	SI
0	    NO
"""

entrada = int(input())

if entrada >= 30400:
    print("SI")
else:
    print("NO")
