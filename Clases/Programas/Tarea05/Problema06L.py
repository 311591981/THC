#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def promedioL():
     L=input("\nIngresa en forma de lista los 10 números para calcular su promedio, i.e. [x1,x2,x3,x4,x5,x6,x7,x8,x9,10]:\n")
     y=0
     while len(L)!=0:
          x=L.pop(0)
          y+=x
     p=y/10.0
     print "\nEl promedio de los 10 números que ingresaste es:\n%.2f" % p
