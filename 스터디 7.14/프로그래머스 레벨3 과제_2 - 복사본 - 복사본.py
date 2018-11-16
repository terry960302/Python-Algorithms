#프로그래머스 레벨3 '멀리뛰기' 문제

from math import factorial as fac

def combination(a,b): #조합 계산하는 함수 
   k=1
   for i in range(0, b):
       k*=(a-i)
   return int(k/fac(b))

def solution(n):
    sum=0
    if n%2==0: #n이 짝수일 경우
        for x in range(0, (n//2)+1):
            sum+=combination(n-x, x)
    else: #n이 홀수일 경우
        for y in range(0, (n//2)+1):
            sum+=combination(n-y, y)
    return sum%1234567
    

#main

n=1700
print(solution(n))

#n=6(짝수)
#[1,1,1,1,1,1]-->6C0==1
#[1,1,1,1,2]-->5C1==5
#[1,1,2,2]-->4C2==6
#[2,2,2]-->3C3==1
#==>13



#return int(k/fac(b))에서
#OverflowError: integer division result too large for a float
