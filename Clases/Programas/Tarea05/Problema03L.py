#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def convertidorCFL():
     L=input('''\nIngresa en forma de lista y en orden "C" si deseas convertir de grados Celsius a grados Fahrenheit o, análogamente,
"F" si deseas convertir de grados Fahrenheit a grados Celsius seguido de la cantidad de grados que deseas convertir, i.e. ["C",x] o
["F",x]:\n''')
     x=L.pop(0)
     y=float(L.pop(0))
     if x=="C":
             z=(y*(9.0/5))+32
             print "\n%.2f°C = %.2f°F\n" % (y,z)
     elif x=="F":
             z=(5*(y)-32)/9.0
             print "\n%.2f°F = %.2f°C\n" % (y,z)
