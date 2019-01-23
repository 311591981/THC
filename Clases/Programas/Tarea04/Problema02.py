#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import math
from math import sqrt

def movimientoparabolicoT():
    y=float(input("\nIngresa la posición del proyectil en metros:\n"))
    v0=float(input('''\nIngresa la velocidad inicial del proyectil en metros sobre segundo:\n'''))
    g=9.81
    if 0<=(pow(v0,2)-(2*g*y)):
        t1=(v0+sqrt((pow(v0,2)-(2*g*y))))/g
    if 0<=(pow(v0,2)-(2*g*y)):
        t2=(v0-sqrt((pow(v0,2)-(2*g*y))))/g
    if 0<=(pow(v0,2)-(2*g*y)):
         print '''\nEl proyectil con velocidad inicial v0 = %.2fm/s alcanza la posición
y = %.2fm en los tiempos T = (%.2fs,%.2fs).\n''' % (v0,y,t1,t2)
    if 0>(pow(v0,2)-(2*g*y)):
         print '''\nLos tiempos en que el proyectil con velocidad inicial v0 = %.2fm/s alcanza la posición
y = %.2fm son numeros complejos por lo tanto T = (t1,t2) no se puede calcular''' % (v0,y)
