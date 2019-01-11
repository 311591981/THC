# -*- coding: utf-8 -*-

# Emilio López Sotelo

# Taréa 1

# En 1687 Newton público su célebre texto titulado "Principios Matemáticos de la Filosofía Natural" donde planteó su hipótesis de la Ley de Gravitación Universal, la cual describe la fuerza de atracción entre dos masas. 
# La Ley de Gravitación Universal está dada por la siguiente ecuación: F = G (Mm / r²), donde F es la fuerza gravitacional que actua entre dos objetos, M y m son las masas respectivas de cada objeto, r es la distancia entre los centros de masa de ambos objetos y G es la constante gravitacional.
# Teniendo esto en cuenta, ¿Cuál es la fuerza de atracción que existe entre el planeta tierra y la luna?
# Antes de enlistar el valor de nuestras variables y contantes cabe aclarar que denotaremos la masa de la tierra como "M" y la masa de la luna como "m".
# Además los datos que se ocupan a continuación han sido redondeados hasta su segundo lugar decimal con el fin de obtener coherencia entre los mismos.

import decimal
from decimal import Decimal

G = Decimal(6.67e-11)
M = Decimal(5.97e+24)
m = Decimal(7.35e+22)
r = Decimal(3844e+2)

F = (G * (M * m / r ** 2))

print F
