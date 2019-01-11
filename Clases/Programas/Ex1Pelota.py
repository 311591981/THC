# -*- coding: utf-8 -*-

#Emilio López Sotelo

#y = (v0 * t) - (1.0/2 * g * t ^ 2)

'''
Información del problema resuelto en este archivo
'''

print (34 * 3) - (1/2 * 9.81 * 3 ** 2) #t=3 #1/2 Calcula la división entera
print
print (34 * 3) - (1.0/2 * 9.81 * 3 ** 2) #t=3 #1.0/2 Calcula la división flotante "real"
print
print (34 * 1) - (1.0/2 * 9.81 * 1 ** 2) #t=1
print
print (34 * 1.5) - (1.0/2 * 9.81 * 1.5 ** 2) #t=1.5
print
print (34 * 5) - (1.0/2 * 9.81 * 5 ** 2) #t=5
print

v0 = 34
g = 9.81
t = 5
y = (v0 * t) - (1.0/2 * g * t ** 2)

print y
