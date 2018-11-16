#연습문제 1번 


f=open('airport.txt')

D={}
for line in f:
    line=line.split()
    D[tuple(line[:3])]=int(line[3])
#여기까지 사전으로 만들기 완료(아마 계속 텍스트 불러오는게 귀찮아서 그런듯)

print('*** Category : city ***')
print()

city={}
for w in D:
    if w[1] not in city:
        city[w[1]]=D[w]
    else:
        city[w[1]]+=D[w]

for m, n in city.items():
    print('{} : {}'.format(m, n))

print()
print()

print('*** Category : status ***')
print()

satus={}
for w in D:
    if w[2] not in satus:
        satus[w[2]]=D[w]
    else:
        satus[w[2]]+=D[w]

for p, q in satus.items():
    print('{} : {}'.format(p, q))
