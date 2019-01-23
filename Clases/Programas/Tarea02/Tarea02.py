#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def Fuerza_Gravedad(M,m,R):
    F = (6.67e-11) * (M) * (m) / (pow(R,2))
    print '''\nEste programa calcula la fuerza de atracción "F", en Newtons(N), entre dos masas "M" y "m", en Kilogramos(Kg), cuyos
centros de masa se encuentran a una distancia "R", en Metros(m), entre si. En base a los valores que has proporcionado y usando
la Ley de Gravitación Universal dada por la ecuacion F = G * (M * m / r ** 2), donde "G" es la constante gravitacional dada por
G = 6.67e-11m³Kg-¹s-², el valor de la fuerza de atracción es:\n\nF = %.2eN\n''' % F
