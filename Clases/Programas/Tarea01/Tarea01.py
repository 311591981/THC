#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

G = 6.67e-11
M = 5.97e+24
m = 7.35e+22
r = 384400000

F = G * (M * m / r ** 2)

print '''\nEste programa calcula la fuerza de atracción entre la Tierra y la Luna,
los datos que se usaron fueron los siguientes:\n
G = 6.67e-11m³Kg-¹s-²          Constante Gravitacional
M = 5.97e+24Kg                     Masa de la Tierra
m = 7.35e+22Kg                     Masa de la Luna
r = 3844e+5m                          Distancia entre los centros de masa
\nutilizamos la Ley de Gravitación Universal dada por la ecuacion:\nF = [G * (M * m / r²)]
\nsustituyendo en la ecuacion tenemos:\nF = {6.67e-11m³Kg-¹s-² * [5.97e+24Kg * 7.35e+22Kg / (3844e+5m)²]}
\nfinalmente se tiene entonces que la fuerza gravitacional es:\n\nF = %.2eN\n''' % (F)
