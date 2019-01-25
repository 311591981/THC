#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def listcheck():
     L=input("\nIngresa en forma de lista ambas listas, i.e. [[A1,A2,...,Ai],[B1,B2,...,Bj]]:\n")
     L1=L.pop(0)
     L2=L.pop(0)
     if L1==L2:
          print "Las listas que ingresaste son iguales, i.e. tienen la misma longitud y sus elementos en cada índice son iguales"
     else:
          print "Las listas que ingresaste no son iguales, i.e. no tienen la misma longitud y sus elementos en cada índice son distintos"
