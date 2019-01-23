#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def Maxcd():
    x=input("\nIngresa el primer número:\n")
    y=input("\nIngresa el segundo número:\n")
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
