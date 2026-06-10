# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:22:29 2026

@author: Darky485
"""

"""
La banana és l'única fruita de l'amor... però el plàtan és de Canàries... Em costa decidir si m'agraden més els plàtans o les bananes.

Entrada
L'entrada consistirà en una sèrie de línies. Cada línia contindrà una lletra P, una lletra B, o 0. El 0 indicarà que hem arribat al final.

Sortida
El programa mostrarà la frase M'agraden els platans si han aparegut més P que B, mostrarà la frase M'agraden les bananes si hi ha més B que P, i mostrarà la frase No puc distingir entre un platan i una banana si el nombre de P és el mateix que el de B.

Exemples
Entrada	| Sortida
P       | M'agraden els platans
B       |
P       |
P       |
B       |
0       |
----------------
B       | No puc distingir entre un platan i una banana
P       |
B       |
B       |
P       |
P       |
0       |
"""

# ENTRADA DE DATOS
bananas, platanos = 0, 0
entrada = input()

# COMPROVAR CONTEO
while entrada != "0":
    if entrada == "P":
        platanos += 1
    elif entrada == "B":
        bananas += 1
        
    entrada = input()

# MOSTRAR RESULTADOS
if bananas < platanos:
    print("M'agraden els platans")
elif bananas > platanos:
    print("M'agraden les bananes")
else:
    print("No puc distingir entre un platan i una banana")
