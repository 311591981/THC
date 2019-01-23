def vAbsoluto(x):
    if x>=0:
        return(x)
    else:
        return(-x)

def raiz(x):
    h=x
    b=1.0
    e=0.0000000001
    while vAbsoluto(b-h)>e:
        h = (b+h)/2
        b = x/h
    return (h)

def raizcontador(x):
    h=x
    b=1.0
    e=0.0000000001
    i=0
    while vAbsoluto(b-h)>e:
        h = (b+h)/2
        b = x/h
        i=i+1
    print "Se ejecuto %i veces el ciclo" % (i)
    return (h)
