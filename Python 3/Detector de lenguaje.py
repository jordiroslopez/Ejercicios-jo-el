# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:00:35 2026

@author: Darky485
"""

"""
En Europa se hablan diversas lenguas cosa que, a veces, hace que sea algo dificil entenderse. Por suerte, cada lengua tiene una manera propia de despedirse i es en ese preciso momento cuando estas seguro de la lengua que estaba usando tu interlocutor. Quizá lo sepas un poco tarde, pero dicen que más vale tarde que nunca.

En castellano, para despedirse se dice "ADIOS".
En anglès, para despedirse se dice "GOOD BYE".
En francès, para despedirse se dice "AU REVOIR"
En italià, para despedirse se dice "CIAO"
En neerlandès, para despedirse se dice "DOEI"
En alemany, para despedirse se dice "TSCHUSS"
Entrada
Cada caso contiene la forma de despedida de alguno de los paises europeos.

Salida
Para cada caso hay que indicar el código ISO del pais al que pertenece la forma de despedida. Si no pertenece a ningún pais reconocido hay que indicar "??"

Los códigos de los paises conocidos son:

España - ES
Inglaterra - UK
Francia - FR
Italia - IT
Paises Bajos - NL
Alemania - DE

Ejemplo de Entrada 1
Adios
Ejemplo de Salida 1
ES

Ejemplo de Entrada 2
CIAO
Ejemplo de Salida 2
IT

Ejemplo de Entrada 3
DOEI
Ejemplo de Salida 3
NL

Ejemplo de Entrada 4
INUULLUARNA
Ejemplo de Salida 4
??
"""

palabra = input().upper()

if palabra == "ADIOS":
    print("ES")
elif palabra == "COOD BYE":
    print("UK")
elif palabra == "AU REVOIR":
    print("FR")
elif palabra == "CIAO":
    print("IT")
elif palabra == "DOEI":
    print("NL")
elif palabra == "TSCHUSS":
    print("DE")
else:
    print("??")
