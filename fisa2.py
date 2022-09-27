import math
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
print('valoarea max=',max(m,n,o))

def min(x,y,z):
    if x<=y and x<=z:
        m=x
    if y<=x and y<=z:
        m=y
    if z<=x and z<=y:
        m=z
    return m 
print('valoarea min=',min(m,n,o))
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

def div(x,y,z):
    divizori=""
    divizor=0
    for i in range(1,(max(x,y,z)+1)):
        if x%i==0 and y%i==0 and z%i==0 and i>divizor:
            divizor=i
            divizori+=str(i)+" "
    return divizori
print('toti divizorii comuni:',div(o,m,n))

def mult(x,y,z):
    multipli=[]
    multiplu=0
    for i in range(1,100000):
        if len(multipli)<3:
            if i*max(x,y,z)%min(x,y,z)==0 :
                multiplu=i*max(x,y,z)
                multipli.append(str(multiplu))
    multipli=' '.join(multipli)
    return multipli
print('3 multipli comuni:',mult(o,m,n))

def semiperimetru(x,y,z):
    s=(x+y+z)/2
    return s 

def triunghi(x,y,z):
    w=[]
    if (x+y)>z and (y+z)>x and (x+z)>y:
        arie='aria='+str(math.sqrt(semiperimetru(x,y,x)*(semiperimetru(x,y,x)-x)*(semiperimetru(x,y,x)-y)*(semiperimetru(x,y,x)-z)))
        perimetru='perimetrul='+str(x+y+z)
    else:
        arie='arie nu exista,'
        perimetru='perimetru nu exista'
    w.extend([arie,perimetru])
    w=' '.join(w)
    return w
print(triunghi(m,n,o))

def ecuatie(x,y,z):
    if ((y**2)-(4*x*z))>=0:
        q=(0-y-math.sqrt((y**2)-(4*x*z)))/(2*x)
        r=(0-y+math.sqrt((y**2)-(4*x*z)))/(2*x)
        sol='x1='+str(q)+', x2='+str(r)
    return sol
print('solutiile ecuatiei ',m,'x**2+',n,'x+',o,'=0 :',ecuatie(m,n,o))


