
l = [-2,-1,0, 1,2,3,4,5,6,7,8,9]

x = (n**2 for n in l)
putin
print (x)
lista = list ()
for elemento in x:
    lista.append(elemento)
for n in x:
    print (n)
    lista.append(n)
print (x)

def meu_xerador (l):
    for n in l:
        yield n**2

v = meu_xerador
print (v)

for n in meu_xerador (l):
    print ("meu_xerador di "+ str(n))






lista = list ()
for elemento in x:
    lista.append(elemento)

tupla = tuple (meu_xerador(l))
print (lista)
print (tupla)