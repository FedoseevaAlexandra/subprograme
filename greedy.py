
'''
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. 
The idea is to sort the arrays and keep track of overlaps.
'''
k=int(input('dati nr de camere din hotel = '))
n=int(input('dati nr de bronari = '))
venire=[]
plecare=[]
for i in range (n):
    venire.append(int(input('dati data de venire: ')))
for i in range (n):
    plecare.append(int(input('dati data de plecare: ')))

def hotel(n,k):
    nr=0
    b=[]
    for i in range (n-1):
        if venire[i+1]>=plecare[i]:
            nr+=1
            b.append(i+1)
        else:
            k-=1
            if k!=0:
                nr+=1
                b.append(i+1)
    return print('numarul maxim de bronari e ',nr+1, ', bronarile posibile sunt cele cu numerele: ',b.append(n-1))
hotel(n,k)