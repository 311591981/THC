C = -20
iC = 5
while C <= 40:
    F = (9.0/5)*C + 32
    print C, F
    #C = C + iC
    C += iC

l=[]
if bool(l) == False:
     print "Esta vacía"
     

S='''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

print S

gradosC = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]

print '    C    F'
for grado in gradosC:
    F = (9.0/5)*grado + 32
    print '%5d %5.1f' % (grado, F)

print S

indice=0

print '    C    F'
while indice<len(gradosC):
     C=gradosC[indice]
     F=(9.0/5)*C + 32
     #print C, F
     #C = C + iC
     print '%5d %5.1f' % (C, F)
     indice+=1

print S

gradosC=[-20]

while gradosC[len(gradosC)-1]!=30:
      gradosC.append(gradosC[len(gradosC)-1]+2.5)
print gradosC
