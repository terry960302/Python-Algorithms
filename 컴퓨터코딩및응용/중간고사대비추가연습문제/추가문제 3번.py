#추가문제 3번

n=int(input('n: '))
x=int(input('x: '))
y=int(input('y: '))

a = 1
while a<=n :
    if x%a == 0 and y%a == 0:
        if a==1:
            a=x*y
k=1
while True:
    a*=k
    print(a)
    k+=1
    if a*k>n:
        break
        
