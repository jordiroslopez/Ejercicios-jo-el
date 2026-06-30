# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:21:27 2026

@author: Darky485
"""

"""
Abans de començar a fer exercicis d'arrays, comprovem que podem llegir i escriure bé en arrays

Entrada
El problema serà de tres línies. La primera tindrà un nombre, K
 que et dirà el tamany de l'array que has de crear La segona son K
 nombres, separats per espais que et dirà el contingut de l'array que has de llegir. La tercera serà N
, una posició de l'array a on has d'accedir. Es garanteix que N<K
.

Sortida
Tornaràs dues linies. La primera serà l'array sencer escrit, amb espais entre cada caràcter. La segona serà el contingut de l'array a la posició N
 (recorda que la primera posició es 0).

Exemple d'Entrada
6
23 2 -4 0 42 69420
2

Exemple de Sortida
23 2 -4 0 42 69420 
-4
"""

longitud = int(input())
array = input().split()
posicion = int(input())

for i in array:
    print(i, end=" ")
print()

print(array[posicion])
