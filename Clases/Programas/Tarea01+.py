# -*- coding: utf-8 -*-

# Taréa 1 - Emilio López Sotelo

import decimal
from decimal import Decimal

G = Decimal(6.67e-11)
M = Decimal(5.97e+24)
m = Decimal(7.35e+22)
r = Decimal(384400000)

F = G * (M * m / r ** 2)

print '''
Este programa calcula la fuerza de atracción entre la Tierra y la Luna,
los datos que se usaron fueron los siguientes:

G = 6.67e-11m³Kg-¹s-²           Constante Gravitacional
M = 5.97e+24Kg                  Masa de la Tierra
m = 7.35e+22Kg                  Masa de la Luna
r = 3844e+5m                    Distancia entre los centros de masa

utilizamos la Ley de Gravitación Universal dada por la ecuacion:

F = [G * (M * m / r²)]

sustituyendo en la ecuacion tenemos:

F = {6.67e-11m³Kg-¹s-² * [5.97e+24Kg * 7.35e+22Kg / (3844e+5m)²]}

finalmente se tiene entonces que la fuerza gravitacional es:

F = %.2eN''' % (F)

print
