#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Emilio López Sotelo, 311591981
Taller de Herramientas Computacionales
--------------------------------------------------------------------------------
Este es un programa que utilizamos para aprender como ejecutar un programa en
python2.7 desde bash.
'''

print "Hoy es miércoles"

#x = 10.5; y = 1.0/3; z = 15.3
x,y,z=10.5,1.0/3,15.3

H = """
El punto en R3 es:
(x,y,z) = (%.2f,%g,%G)
""" % (x,y,z)

print H

G ="""
El punto en R3 es:
(x,y,z) = ({laX:.2f},{laY:g},{laZ:G})
""".format(laX=x,laY=y,laZ=z)

print G

import math
from math import sqrt as s


x=16

x=input("Cual es el valor al que le quieres calcular la raíz?\n")

print "La raíz cuadrada de %.2f es:\n%f" % (x,s(x))

y=input("Cual es el valor al que le quieres calcular la raíz?\n")

print "La raíz cuadrada de %.2f es:\n%f" % (y,s(y))
