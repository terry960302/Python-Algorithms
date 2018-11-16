#중국어문화학과 2017650009 김태완

import math
num_total=-1
num_square=0

while True:
    n=int(input('Enter n: '))
    num_total+=1
    if n==0:
        print('-'*30)
        break
    else:
        k=math.sqrt(n)    
        if k==int(k):
            print('{} is perfect square of {}'.format(n,int(k)))
            num_square+=1
        else:
            print('{} is not perfect square number'.format(n))
                   
print('You entered total {} numbers.'.format(num_total))
print('There are {} square numbers.'.format(num_square))


        


    
