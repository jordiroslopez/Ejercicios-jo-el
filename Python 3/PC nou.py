# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:07:26 2026

@author: Darky485
"""

"""
En Pere vol comprar un pc nou. Fes un programa que demani, en una sola línia, el preu del pc i el sou mensual d'en Pere. S'ha de calcular quants dies ha d'estalviar per poder comprar-lo.

Suposarem que els mesos tenen 30 dies.

Entrada
Cada cas és d'una sola línia que contindrà el preu i el sou, separats per un espai.

Sortida
Una línia tal com "En Pere ha d'estalviar durant N dies", on N és un nombre enter positiu.

Exemples
Entrada	 | Sortida
1345 900 | En Pere ha d'estalviar durant 45 dies
"""

DURACION_MES = 30

# DATOS DE ENTRADA
entrada = input().split()
precio = float(entrada[0])
sueldo = float(entrada[1])

ahorro = int((precio // (sueldo / DURACION_MES)) + 1) # CALCULO AHORRO

print(f"En Pere ha d'estalviar durant {ahorro} dies") # IMPRESION DE RESULTADO
