# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:29:20 2026

@author: Darky485
"""

"""
Ja saps escriure arrays d'enters. Ara escriurem arrays de Strings.

Entrada
El problema serà de múltiples línies. La primera tindrà un nombre, K
 que et dirà el tamany de l'array que has de crear després vindran K
 línies, tantes com el tamany de l'array, amb una String cadascuna L'última serà N
, una posició de l'array a on has d'accedir. Es garanteix que N<K
.

Sortida
Tornaràs K+1 linies. Primer serà l'array sencer escrit, amb salt de línea entre cada string. La segona serà el contingut de l'array a la posició N
 (recorda que la primera posició es 0).

Exemple d'Entrada
6
HOLA
MARC
KERNEL
POMES
PREFERIRIA ESTAR JUGANT AL FACTORIO ABANS QUE FER AQUEST EXERCICI
COM A MINIM FINS QUE SURTI SHADOWLANDS.
4

Exemple de Sortida
HOLA
MARC
KERNEL
POMES
PREFERIRIA ESTAR JUGANT AL FACTORIO ABANS QUE FER AQUEST EXERCICI
COM A MINIM FINS QUE SURTI SHADOWLANDS.
PREFERIRIA ESTAR JUGANT AL FACTORIO ABANS QUE FER AQUEST EXERCICI
"""

n = int(input())
array = []

for i in range(n):
    array.append(input())

p = int(input())

for i in range(n):
    print(array[i])

print(array[p])






















