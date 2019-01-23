#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import Grados
from Grados import listaC
from Grados import listaF
from Grados import mostrarlistas
from Grados import mostrarlistas1

L1 = listaC(-15,32,10)
L2 = listaF(L1)
mostrarlistas(L1,L2)
mostrarlistas1(L1,L2)

a = input("¿Cual es el extremo izquierdo del intervalo?")
b = input("¿Cual es el extremo derecho del intervalo?")
n = input("¿Cuantos subintervalos?")
L1 = listaC(a,b,n)
L2 = listaF(L1)
mostrarlistas(L1,L2)

