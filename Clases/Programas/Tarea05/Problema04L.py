#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def Frec(n):
        if n<2:
            return n
        else:
            return Frec(n-1)+Frec(n-2)

def sfiboL():
     L=input('''\nIngresa en forma de lista el enesimo término de la serie de Fibonacci que deseas encontrar, i.e. [n]:\n''')
     x=L.pop(0)
     print '\nEl %d° término de la serie de Fibonacci es:\n%d\n' % (x,Frec(x))
