# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:55:49 2026

@author: Darky485
"""

"""
Dos nens petits discuteixen per qui té l'avi més gran. Ajuda'ls

Entrada
El programa llegeix els noms i les edats (valors enters) dels dos avis.

Sortida
El programa informa amb el nom de l'avi més vell. Si els dos tenen la mateixa edat dirà: "Cap es mes vell".

Aquí et presento algunes instruccions que pots fer servir:

Instrucció	Descripció
nom = input()	Guarda a la variable nom la cadena de caràcters que hagis introduït per teclat
edat = int(input())	Permet llegir de teclat un nombre enter i ho guarda dins d’edat
print(nom)	Ensenya per pantalla el valor posat en nom.
 if (valor1 < valor2):
     print(“valor1 és més petit”)
elif (valor1 > valor2):
     print(“valor2 és més petit”)
else:
     print(“Els dos valors són iguals”)

Instrucció condicional anuada. Com funciona? Pregunta si valor1 < valor2.
Si la resposta és correcta, es mostra per pantalla “valor1 és més petit”.
Però, si la resposta és falsa, llavors, entra en el següent if (elif) i torna a fer el mateix:
Si la pregunta valor1 > valor2 és certa, mostra “valor2 és més petit”, i
si no fos certa, mostra: “Els dos valors són iguals”
Pista!
El programa són màxim 10 línies: les 4 primeres llegeixen les edats i els noms dels avis. Les 6 següents comparen les edats i mostren el resultat adient. Vigila molt en respectar les tabulacions dins de if, elif i else. Recorda que if, elif i else finalitzen sempre la línia amb ':'

Exemples
----------------
Entrada
Martí
78
Joan
69

Salida
Marti
----------------
Entrada
Marina
64
Anna
80

Salida
Anna
----------------
Entrada
Josep
78
Carles
78

Salida
Cap es mes vell
----------------
"""

# PERSONA 1
nom_1 = input()
edat_1 = int(input())

# PERSONA 2
nom_2 = input()
edat_2 = int(input())

# CALCULO DE EDAD
if (edat_1 > edat_2):
    print(nom_1)
elif (edat_1 < edat_2):
    print(nom_2)
else:
     print('Cap es mes vell')
