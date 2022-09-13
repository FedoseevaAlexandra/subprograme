def creare_lista():
    n=int(input('dati nr de elemente: '))
    lista_creata=[]
    for i in range(n):
        element=eval(input('elementul '+str(i)+' este: '))
        while type(element)!=int:
            element=eval(input('Introduceti doar elemente de tip int! Elementul '+str(i)+' este: '))
            if type(element)==int:
                break
        lista_creata.append(element)
    return lista_creata
lista1=creare_lista()
print(lista1)
