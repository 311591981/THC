#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

LX=[]
x=-5
while x<=5:
     Lx=[x]
     x+=0.5
     LX.append(Lx)
     
LYU=[]
y=-7
while y<=7:
     Lyu=[y]
     y+=1.5
     LYU.append(Lyu)

LYD=[]
y=7
while y>=-7:
     Lyd=[y]
     y-=1.5
     LYD.append(Lyd)
     
LYD.append([0]);LYU.extend(LYD);LYU.sort()
LY=LYU

Malla=[]
i=-1
j=0
j1=-1

"""while i<len(LX):
     i+=1
     for x in LX:
          L=[[LX[i][0],LY[j][0]]]
          Malla.extend(L)
          j+=1"""

while i<len(LX):
     i+=1
     j1+=1
     j=j1
     while j<len(LY):
          L=[[LX[i][0],LY[j][0]]]
          Malla.extend(L)
          j+=1
