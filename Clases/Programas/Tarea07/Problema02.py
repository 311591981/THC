#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def matrix():
     matriz=input('''\nIngresa en forma de una lista de listas una matriz de enteros, i.e.
[[A11,A12,...,A1j],[A21,A22,...,A2j],[...,...,...,...],[Ai1,Ai2,...,Aij]] donde Aij,Bij son enteros para todo i,j:\n''')
     matrizr=matriz
     matrizc=
     matrizsr=[]
     matrizsc=[]
     dim=input("\nIngresa en forma de lista las dimensiones de la matriz, i.e. [M,N]:\n")
     M=dim.pop(0)
     N=dim.pop(0)
     i=1
     j=1
     while i<=M:
          sumar=(sum(matrizr[i-1]))
          matrizsr.append(sumar)          
          i+=1
          print matrizsr
     while j<=N:
          sumac=(sum(matrizsc[j-1]))
          matrizsc.append(sumar)
          j+=1
