# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:37:08 2026

@author: Darky485
"""

"""
Dues persones estan discutin respecte a quina de les seves cases es més gran. Fes un programa que els ajudi a resoldre el problema.

Entrada
El programa llegeix en una linia el nom de la persona i en una segona linia el número de pisos de la casa (entre 1 i 3), l'amplada i la llargada de cada pis (separats per espais).

Sortida
El programa informa amb el nom de la persona amb més metres quadrats de casa. S'ha de tenir en compte que els pisos d'una mateixa casa medeixen igual. En el cas que siguin iguals mostrarà un missatge del tipus: "Les dues cases son igual de grans".

Exemples:
----------------
Entrada
Pere
2 20 5
Maria
3 10 20

Sortida
Maria
----------------
Entrada
Anna
2 2.5 5
Elsa
2 2 5

Sortida
Anna
----------------
Entrada
Laura
2 2 5
Carles
2 2 5

Sortida
Les dues cases son igual de grans
----------------
"""

# DATOS PERSONA 1
persona_1 = input()
medidas = input().split()
pisos_1 = float(medidas[0])
ancho_1 = float(medidas[1])
largo_1 = float(medidas[2])

# DATOS PERSONA 2
persona_2 = input()
medidas = input().split()
pisos_2 = float(medidas[0])
ancho_2 = float(medidas[1])
largo_2 = float(medidas[2])

# CALCULO DE MEDIDAS
if (pisos_1 * ancho_1 * largo_1 > pisos_2 * ancho_2 * largo_2):
    print(persona_1)
elif (pisos_1 * ancho_1 * largo_1 < pisos_2 * ancho_2 * largo_2):
    print(persona_2)
else:
    print('Les dues cases son igual de grans')
