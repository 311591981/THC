# -*- coding: utf-8 -*-

# Taréa 1 - Emilio López Sotelo

#En 1687 Newton público su célebre texto titulado "Principios Matemáticos de la
#Filosofía Natural" donde planteó su hipótesis de la Ley de Gravitación Universal
#la cual describe la fuerza de atracción entre dos masas. La Ley de Gravitación
#Universal está dada por la ecuación: F = G (Mm / r²), donde F (con unidades en
#Newtons o N) es la fuerza gravitacional que actua entre dos objetos, M y m (con
#unidades en Kilogramos o Kg) son las masas respectivas de cada objeto, r (con
#unidades en metros o m) es la distancia entre los centros de masa de ambos
#objetos y G (con unidades m³Kg-¹s-²) es la constante gravitacional. Teniendo
#esto en cuenta, ¿Cuál es la fuerza de atracción que existe entre el planeta
#Tierra y la Luna? Antes de enlistar el valor de nuestras variables y constantes
#cabe aclarar que denotaremos la masa de la Tierra como "M" y la masa de la Luna
#como "m". Además los datos que se ocupan a continuación han sido redondeados a
#su segundo lugar decimal con el fin de obtener consistencia entre los mismos.

import decimal
from decimal import Decimal

G = Decimal(6.67e-11)
M = Decimal(5.97e+24)
m = Decimal(7.35e+22)
r = Decimal(384400000)

F = G * (M * m / r ** 2)

print '''
Este programa calcula la fuerza de atración entre la Tierra y la Luna,
los datos que se usaron fueron los siguientes:

G = 6.67e-11m³Kg-¹s-²           Constante Gravitacional
M = 5.97e+24Kg                  Masa de la Tierra
m = 7.35e+22Kg                  Masa de la Luna
r = 3844e+5m                    Distancia entre los centros de masa

utilizando la Ley de Gravitación Universal dada por la ecuacion:

F = [G * (M * m / r²)]

sustituyendo en la ecuacion tenemos:

F = {6.67e-11m³Kg-¹s-² * [5.97e+24Kg * 7.35e+22Kg / (3844e+5m)²]}

finalmente se tiene entonces que la fuerza gravitacional es:

F = %.2eN''' % (F)

print
