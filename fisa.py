m=int(input('primul nr='))
n=int(input('al doilea nr='))
o=int(input('al treilea nr='))
def max(x,y,z):
    if x>=y and x>=z:
        m=x
    if y>=x and y>=z:
        m=y
    if z>=x and z>=y:
        m=z
    return m 
print('valoarea max=')

def min(x,y,z):
    if x<=y and x<=z:
        m=x
    if y<=x and y<=z:
        m=y
    if z<=x and z<=y:
        m=z
    return m 
print('valoarea min=')
def a(x,y,z):
    divizor=0
    for i in range(1,(min(x,y,z)+1)):
        if x%i==0 and y%i==0 and i>divizor and z%i==0:
            divizor=i
    return divizor
print('Cel mai mare divizor comun =',a(m,n,o))

def b(x,y,z):
    multiplu=0
    mult=0
    for i in range(1,100):
        if i*max(x,y,y)%min(x,y,y)==0: 
            multiplu=i*max(x,y,y)
            if i*max(multiplu,z,z)%min(multiplu,z,z)==0: 
              mult=i*max(multiplu,z,z)
            return mult
print('cel mai mic multiplu comun =',b(o,m,n))

