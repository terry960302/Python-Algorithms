#중국어문화학과 2017650009 김태완

print('-'*30)
print('< 사전 D1  출력 >')
print('-'*30)

f=open('score.txt')

D1={}
for line in f:
    items=line.split()
    for i in range(1,5):
        items[i]=int(items[i])
        k,v=items[0], items[1:]
        D1[int(k)]=v
    print('{} {}'.format(k, v))

print('-'*30)
print('< 사전 D2  출력 >')
print('-'*30)

D2={}

for key in D1:
    D2[key]=sum(D1[key])/4
for m, n in D2.items():
    print('{} - {:.2f}'.format(m, n))




