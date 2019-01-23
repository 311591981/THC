alumnos = []
alumnos.append([9, 8, 10, 9])
alumnos.append([9])
alumnos.append([6, 9, 10, 8, 9, 10, 10, 9])

for i in range(len(alumnos)):
     for j in range(len(alumnos[i])):
          calificacion = alumnos[i][j]
          print "%4d" % calificacion,
     print

for i in alumnos:
     for j in i:
          print "%4d" % j,
     print

L=[]
ALUMNO=["EMILIO","JUAN","XIMENA","JAIME","SOFIA"]
SEMESTRE=[1]
MATERIAS=["ALGEBRA","CALCULO","GEOMETRIA","DISCRETAS"]
CALIFICACIONES=[[6,7,8,9],[10,9,8,7],[8,6,7,9],[


