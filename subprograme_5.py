a=int(input())
b=int(input())
c=int(input())
d=int(input())
def adunarea(w,x,y,z):
    s=(w*z+y*x)/(x*z)
    return s
print('adunarea:',adunarea(a,b,c,d))
def inmultirea(w,x,y,z):
    i=(y*w)/(x*z)
    return i
print('inmultirea:',inmultirea(a,b,c,d))
