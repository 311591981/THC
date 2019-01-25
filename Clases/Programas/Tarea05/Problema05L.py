#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def sumaprimerosnL():
     L=input('''\nIngresa en forma de lista el enésimo término hasta donde quieres sumar, i.e. [n]:\n''')
     x=L.pop(0)
     i=1
     s=0
     while i<=x:
          s+=1*i
          i+=1
     print '''\nLa suma de los primeros %d números naturales es:\n%d\n''' % (x,s)
