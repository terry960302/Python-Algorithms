#실습문제 8번-2번

def isprime(a):
    if a==1:
        return False
    for i in range(2, a):
        if a%i==0:
            return False
    return True

#main

n=int(input('Enter n: '))

if isprime(n)==True:
    print('{} is prime.'.format(n))
else:
    print('{} is not prime'.format(n))

