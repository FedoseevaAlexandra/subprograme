'''O gradina zoologica poate acomoda un numar maxim de N animale de aceeasi specie (limita). O alta gradina zoologica s-a inchis, iar animalele de acolo trebuie transferate de urgenta. Se stie numarul de animale deja prezente in gradina si speciile acestora (ele nu pot fi separate).
 Sa se afle care specii de animale vor putea fi transferate si ate animale de fieare fel vor fi la gradina zoologica.'''
specii=['pantere = ','antilope = ','alpacca = ','hipopotami = ','vulturi = ','crocodili = ']
nrin=[]
nrtr=[]
print('initial erau:')
for i in specii:
    nrin.append(int(input(i)))
print('este nevoie de a fi transferate:')
for i in specii:
    nrtr.append(int(input(i)))
limita=int(input('limita de capete per specie este de: '))
def Sol_Pos(a):    
	if nrin[a]+nrtr[a]<=limita:       
		return True    
	else:       
		return False

def Prel_Sol_True(a): 
    n=nrtr[a]+nrin[a]     
    return print('In urma tranferului vor fi: ', n, specii[a].rstrip('= '))

def Prel_Sol_False(a): 
    n=nrin[a]     
    return print('Vor ramane: ', n, specii[a].rstrip('= ')) 

for a in range (len(specii)):                        
    if (Sol_Pos(a)):                        
       Prel_Sol_True(a)
    else:
      Prel_Sol_False(a)
