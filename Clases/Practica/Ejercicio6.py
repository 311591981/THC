#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def nfactorial(n):
     '''Ingresa un numero natural para conocer su factorial'''
     if n<2:
          return 1
     else:
          return n*nfactorial(n-1)
