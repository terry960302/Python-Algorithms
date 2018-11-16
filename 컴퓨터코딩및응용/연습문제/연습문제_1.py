print('*** Category : city ***')
print()
f=open('airport.txt', 'r')

D={}
for line in f:
    L=line.split()
    if L[1] not in D:
        D[L[1]]=int(L[3])
    else:
        D[L[1]]+=int(L[3])

for m, n in D.items():
    print('{} : {}'.format(m,n))

print()

print('*** Category : status ***')
print()
f=open('airport.txt', 'r')
D2={}
for line in f:
    L=line.split()
    if L[2] not in D2:
        D2[L[2]]=int(L[3])
    else:
        D2[L[2]]+=int(L[3])

for p, q in D2.items():
    print('{} : {}'.format(p,q))
