#중국어문화학과 2017650009 김태완

while True:
    n=int(input('Enter n: '))
    if n<0:
        print('should input 0 or positive integer.')
        break
    if n==0:
        print('{}! = {}'.format(n, 1))
    a=1
    mul=1
    while a<=n:
        mul*=a
        a+=1
        if a==n+1:
            print('{}! = {}'.format(n, mul))
