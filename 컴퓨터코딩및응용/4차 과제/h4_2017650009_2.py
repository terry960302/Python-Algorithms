#중국어문화학과 2017650009 김태완

L=[]
for i in range(10):
    k=int(input('Enter data {}: '.format(i)))
    L.append(k)

M=[]
for a in range(9):
    b=abs(L[a+1]-L[a])
    M.append(b)
    largest=M[0]
for c in M[1:]:
    if c>=largest:
        largest=c
        

print('L: {}'.format(L))
print('{}와 {} 사이의 절대값 차가 {}로 가장 크다'.format(M.index(largest), M.index(largest)+1, largest))




