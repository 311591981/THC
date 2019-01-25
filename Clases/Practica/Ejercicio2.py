#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def suma_primeros_n_al_cuadrado(n):
     '''Ingresa un número natural para conocer la suma de los primeros n²'''
     if n<2:
          return 1
     else:
          return pow(n,2)+suma_primeros_n_al_cuadrado(n-1)

def comprobacion_cuadrado(n):
     return (n*(n+1)*((2*n)+1))/6
