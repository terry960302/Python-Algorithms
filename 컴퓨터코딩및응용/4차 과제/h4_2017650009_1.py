#중국어문화학과 2017650009 김태완


ten=[]
eng='st'

for k in range(1,11):
    i=int(input('Enetr {}{} integer: '.format(k, eng)))
    if k==1:
        eng='nd'
    elif k==2:
        eng='rd'
    else:
        eng='th'
    if i>0:
        ten.append(i)
    k+=1

print('ten: {}'.format(ten))
print('sum :{}'.format(sum(ten)))
print('len: {}'.format(len(ten)))

