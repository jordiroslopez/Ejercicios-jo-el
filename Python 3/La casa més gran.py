# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:37:08 2026

@author: Darky485
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
