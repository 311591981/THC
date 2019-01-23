#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def Frec(n):
        if n<2:
            return n
        else:
            return Frec(n-1)+Frec(n-2)

def sfibo():
    n=int(input('''\nIngresa el enesimo término de la serie de Fibonacci que
deseas encontrar:\n'''))
    print '\nEl %d° término de la serie de Fibonacci es:\n%d\n' % (n,Frec(n))
