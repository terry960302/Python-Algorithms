# hackerranks medium 'Extra long factorials' 풀이1

def extralongFactorials(n):
    if 1<= n <= 100:
        mul=1
        for i in range(1, n+1):
            mul*=i
    return mul

#main

n=int(input('Enter n: '))
print(extralongFactorials(n))
