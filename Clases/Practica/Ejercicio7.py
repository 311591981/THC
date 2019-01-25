#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy
from numpy import sin
from numpy import pi

def H_eps(x,eps=0.01):
     if x<-eps:
          return 0
     elif -eps<=x<=eps:
          return 0.5+(x/(2*eps)+((1/(2*eps))*sin((pi*x)/eps)))
     elif x>eps:
          return 1

def prueba_H_eps():
     eps=0.01
     x1=-1
     x2=-eps
     x3=0
     x4=eps
     x5=1
     print H_eps(x1,eps)
     print H_eps(x2,eps)
     print H_eps(x3,eps)
     print H_eps(x4,eps)
     print H_eps(x5,eps)
