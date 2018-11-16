        
num_total=-1
num_square=0

while True:
    n=int(input('Enter n: '))
    num_total+=1
    if n==0:
        print('-'*30)
        break
    else:
        a=1
        while a<=n:
            a+=1
            
            if n==a**2:
                print('{} is perfect square of {}'.format(n,a))
                num_square+=1
                break
        else:
            print('{} is not perfect square number'.format(n))

print('You entered total {} numbers.'.format(num_total))
print('There are {} square numbers.'.format(num_square))
