#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def maxminprom():
    y1=float(input("\nIngresa el 1° número:\n"))
    y2=float(input("\nIngresa el 2° número:\n"))
    y3=float(input("\nIngresa el 3° número:\n"))
    y4=float(input("\nIngresa el 4° número:\n"))
    y5=float(input("\nIngresa el 5° número:\n"))
    y6=float(input("\nIngresa el 6° número:\n"))
    y7=float(input("\nIngresa el 7° número:\n"))
    y8=float(input("\nIngresa el 8° número:\n"))
    y9=float(input("\nIngresa el 9° número:\n"))
    y10=float(input("\nIngresa el 10° número:\n"))
    z1=max(y1,y2,y3,y4,y5,y6,y7,y8,y9,y10)
    z2=min(y1,y2,y3,y4,y5,y6,y7,y8,y9,y10)
    z3=(y1+y2+y3+y4+y5+y6+y7+y8+y9+y10)/10
    print "\nEl número mas grande que ingresaste es:\n%.2f" % z1
    print "\nEl número mas pequeño que ingresaste es:\n%.2f" % z2
    print "\nEl promedio de los 10 números que ingresaste es:\n%.2f" % z3
    
