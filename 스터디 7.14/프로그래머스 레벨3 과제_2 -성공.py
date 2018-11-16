#프로그래머스 레벨3 '멀리뛰기' 문제

def fivonacci(k):
    L=[0,1]
    if 2 <= k <= 100000:
        for i in range(k):
            L.append(L[i]+L[i+1])
    return L[k+1]%1234567
    

#main

n=1700
print(fivonacci(n))

