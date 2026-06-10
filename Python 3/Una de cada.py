# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:44:27 2026

@author: Darky485
"""

"""
Tothom sap que normalment les paraules s'escriuen en minúscules, amb algunes excepcions, és clar.

Com tenim esperit revolucionari farem la nostra pròpia norma. Quan haguem d'escriure un paràgraf, format per una o més frases, començarem escrivint en minúscules i anirem alternant cada lletra escrivint majúscula i minúscula. Evidentment, els signes de puntuació són indiferents a la capitalització.

Escriu un programa que comença llegint un número enter major o igual que 0, i a continuació rep la quantitat indicada de línies de text no buides.

El programa mostrarà les línies tal i com les ha llegit però aplicant la nostra normativa alternada.

Entrada
Un número enter major o igual que 0 i menor que 1000, que li direm n, seguit d'n línies de text no buides (tenen algun caràcter diferent a l'espai en blanc i salt de línia)

Sortida
n línies de text contenint el mateix text que s'ha llegit, però havent aplicat la nostra normativa

Exemple d'Entrada
4
There's a lady who's sure
all that glitters is gold
And she's buying
a stairway to heaven

Exemple de Sortida
tHeRe's a lAdY WhO'S SuRe
AlL ThAt gLiTtErS Is gOlD
aNd sHe's bUyInG
a sTaIrWaY To hEaVeN
"""

n = int(input())
contador = True

for _ in range(n):
    texto = input()
    
    for letra in texto:
        if letra != "\n":
            if contador == False:
                contador = True
                l = letra.upper()
            else:
                contador = False
                l = letra.lower()
        else:
            l = "\n"
        print(l, end="")
