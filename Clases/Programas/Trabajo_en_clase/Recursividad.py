def fib(n):
     """Calcula el enesimo termino de la sucesion de Fibonacci con n natural"""
     if n>2:
          return fib(n-1)+fib(n-2)
     else:
          return 1

def sigman(n):
     """Calcula la suma de los primeros n números naturales"""
     if n>1:
          return n + sigman(n-1)
     else:
          return 1

def printR(L):
     if len(L)>1:
          print L[0],
          printR(L[1:])
     else:
          print L[0]
