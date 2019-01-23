#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def MaxcdL():
     L=input("\nIngresa en forma de lista ambos números, i.e. [a,b]:\n")
     x=L.pop(0)
     y=L.pop(0)
     a=x
     b=y
     if x<y:
          z=y
          y=x
          x=z
     res=x%y
     while res!=0:
          x=y
          y=res
          res=x%y
     print "\nEl MCD entre %d y %d es:\n%d\n" % (a,b,y)
