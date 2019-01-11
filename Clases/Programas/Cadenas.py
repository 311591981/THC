i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field

print '"%d"' % i       # minimum field

#Se imprime un numero entero

print '"%5d"' % i      # field of width 5 characters

#Se imprime sobre el espacio de 5 caracteres

print '"%05d"' % i     # pad with zeros

#Se imprime sobre el espacio de 5 caracteres pero rellena los espacios vacios
#con 0's

print '"%g"' % r       # r is big number so this is scientific notation

#Se imprimen hasta 6 caracteres con redondeo incluido y con el exponente e

print '"%G"' % r       # E in the exponent

#Se imprimen hasta 6 caracteres con redondeo incluido y con el exponente E

print '"%e"' % r       # compact scientific notation

#Se imprime en notacion scientifica compacta con el exponente e

print '"%E"' % r       # compact scientific notation

#Se imprime en notacion scientifica compacta con el exponente E

print '"%20.2E"' % r   # 2 decimals, field of width 20

#Se imprime hasta 2 decimales sobre el espacio de 20 caracteres

print '"%30g"' % r     # field of width 30 (right-adjusted)

#Se imprime sobre el espacio de 30 caracteres ajustado hacia la derecha

print '"%-30g"' % r    # left-adjust number

#Se imprime sobre el espacio de 30 caracteres ajustado hacia la izquierda

print '"%-30.4g"' % r  # 3 decimals

#Se imprime hasta 3 decimales sobre el espacio de 30 caracteres ajustado hacia
#la izquierda

print '%s' % i   # can convert i to string automatically

#Se imprime como una cadena

print '%s' % r

#se imprime como una cadena

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)

#el %% imprime el simbolo de %
