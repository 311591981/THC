#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def convertidorCF():
    x=input('''\nIngresa "C" si deseas convertir de grados Celsius a
grados Fahrenheit o ,análogamente, ingresa "F" si deseas convertir de grados
Fahrenheit a grados Celsius:\n''')
    y=input("\nIngresa la cantidad de grados que deseas convertir:\n")
    if x=="C":
        z=(y*(9.0/5))+32
        print "\n%.2f°C = %.2f°F\n" % (y,z)
    elif x=="F":
        z=(5*(y)-32)/9.0
        print "\n%.2f°F = %.2f°C\n" % (y,z)
