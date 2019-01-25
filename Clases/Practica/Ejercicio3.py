#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def suma_primeros_n_al_cubo(n):
     '''Ingresa un número natural para conocer la suma de los primeros n³'''
     if n<2:
          return 1
     else:
          return pow(n,3)+suma_primeros_n_al_cubo(n-1)

def comprobacion_cubo(n):
     return pow(((n*(n+1))/2),2)
