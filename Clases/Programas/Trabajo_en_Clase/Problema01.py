#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def mcd(a,b):
    if a<b:
        tmp=b
        b=a
        a=tmp
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
