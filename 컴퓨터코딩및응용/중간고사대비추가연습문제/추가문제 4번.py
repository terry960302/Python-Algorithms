#추가문제 4번

n=int(input('Enter n: '))


#1부터 k까지의 합
#if 합이 n을 넘기면 넘는 순간의 k반환하고 합도 반환

a=1
sum=0

while True:
    sum+=a
    a+=1
    if sum>n:
        print('1부터 {}까지의 합은 {}이다.'.format(a-1, sum))
        break



