#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def sumaprimerosn():
    n=input('''\nIngresa el enésimo término hasta donde quieres sumar\n''')
    i=1
    s=0
    while i<=n:
        s+=1*i
        i+=1
    print '''\nLa suma de los primeros %d números naturales es:\n%d\n''' % (n,s)
