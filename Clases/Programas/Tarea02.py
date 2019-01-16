# -*- coding: utf-8 -*-

# Taréa 1 - Emilio López Sotelo

import math
import decimal
from decimal import Decimal

def Fuerza_Gravedad(M,m,R):
    F = (Decimal(6.67e-11)) * (Decimal(M) * Decimal(m) / Decimal(math.pow(R,2)))
    print '''Este programa calcula la fuerza de atracción "F" entre dos masas "M" y "m"
cuyos centros de masa estan a una distancia "R" entre si, en base a los valores
que has proporcionado el valor de la fuerza es:'''
    print "F = %.2eN" % F
