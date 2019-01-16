# -*- coding: utf-8 -*-

# Emilio López Sotelo

# Taréa 1

import decimal
from decimal import Decimal

G = Decimal(6.67e-11)
M = Decimal(5.97e+24)
m = Decimal(7.35e+22)
r = Decimal(3844e+5)

F = (G * (M * m / r ** 2))

print "F =%.2eN" % F
