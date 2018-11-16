#컴응 실기 연습문제 1번

f=open('airport.txt')

#텍스트 파일 사전으로 만들기(code, city, status : number_of_flights)

D={}
for line in f:
    line=line.split()
    D[tuple(line[:3])]=int(line[3])


#############################

print('*** Category : city ***')
print()

city={}
for a in D:
    if a[1] not in city:
        city[a[1]]=D[a]
    else:
        city[a[1]]+=D[a]
for m,n in city.items():
    print('{} : {}'.format(m, n))
print()
print('*** Category : status ***')
print()

status={}
for b in D:
    if b[2] not in status:
        status[b[2]]=D[b]
    else:
        status[b[2]]+=D[b]
for p,q in status.items():
    print('{} : {}'.format(p, q))
