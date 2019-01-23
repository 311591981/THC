def ulam(x):
    if x % 2 == 0:
        return x/2
    else:
        return (3*x)+1

def suc(x):
    i=0
    while x!=1:
        x=ulam(x)
        i=i+1
    return i
