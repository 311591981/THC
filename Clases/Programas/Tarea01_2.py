# -*- coding: utf-8 -*-

# Taréa 1 - Emilio López Sotelo

'''
En 1687 Newton público su célebre texto titulado "Principios Matemáticos de la
Filosofía Natural" donde planteó su hipótesis de la Ley de Gravitación Universal
la cual describe la fuerza de atracción entre dos masas. La Ley de Gravitación
Universal está dada por la ecuación: F = G (Mm / r²), donde F (con unidades en
Newtons o N) es la fuerza gravitacional que actua entre dos objetos, M y m (con
unidades en Kilogramos o Kg) son las masas respectivas de cada objeto, r (con
unidades en metros o m) es la distancia entre los centros de masa de ambos
objetos y G (con unidades m³Kg-¹s-²) es la constante gravitacional. Teniendo
esto en cuenta, ¿Cuál es la fuerza de atracción que existe entre dos masas?
'''

import math
import decimal
from decimal import Decimal

def Fuerza_Gravedad(M,m,R):
    F = (Decimal(6.67e-11)) * (Decimal(M) * Decimal(m) / Decimal(math.pow(R,2)))
    print '''Este programa calcula la fuerza de atracción "F" entre dos masas "M" y "m"
cuyos centros de masa estan a una distancia "R" entre si, en base a los valores
que has proporcionado el valor de la fuerza es:'''
    print "F = %.2eN" % F
    return;
