# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:31:25 2026

@author: Darky485
"""

"""
Mis alumnos de primero estan aprendiendo a programar y, muy de tanto en tanto, le preguntan al ChatGPT y se copian alguna barbaridad. Hay profesores que dicen que hacen "terrorismo". Yo soy más sutil y les digo que han hecho una máquina del tiempo. ¿Cómo que una máquina del tiempo? me preguntan ellos. Y yo, que ya me espero su pregunta, les digo "Sí, como te lo vuelva a ver te vas a ir directo a la recuperación de junio!"

Ejemplos de máquina del tiempo son:

while (true) y salir con un break
cambiar la variable de iteración dentro de un for
hacer funciones con más de un return
usar continue o break dentro de un bucle
finalizar la función main() con return o System.exit()
Como que en el ITB nos gusta hacer todo tipo de inventos, cualquier día de estos conseguiremos hacer una máquina de tiempo de verdad. El dia que la pongamos en marcha, dependiendo de como funcione la máquina y del año al que vayamos a parar, quizá nos vayamos al otro barrio. No nos pongamos dramáticos que seguro que no se muere nadie. Lo que ocurre es que hace 40 años el ITB no estaría en Nou Barris, sinó en Sant Andreu. Nou Barris no se constituyó como distrito hasta el año 1984. Hasta aquel año todos los barrios que conforman Nou Barris pertenecían a Sant Andreu.

Entrada
Cada caso contiene un número con el año de destino de nuestro viaje en el tiempo.

Salida
Hay que indicar "Sant Andreu" o "Nou Barris" dependiendo del distrito donde apareceríamos.

Ejemplo de entrada 1
1980
Ejemplo de salida 1
Sant Andreu
Ejemplo de entrada 2
2050
Ejemplo de salida 2
Nou Barris
"""

entrada = int(input())

if entrada < 1984:
    print("Sant Andreu")
else:
    print("Nou Barris")
