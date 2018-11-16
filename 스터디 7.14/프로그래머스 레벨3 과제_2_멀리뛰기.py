#프로그래머스 레벨3 '멀리뛰기' 문제

from math import factorial as fac #팩토리얼 모듈

def combination(a,b): #조합(콤비네이션) 함수
    return fac(int(a))/fac(int(b))/fac(int(a)-int(b))

def solution(n):
    sum=0
    for i in range(0, (n//2)+1):
        sum+=combination(n-i,i)
    return int(sum)%1234567

#main

n=1700
print(solution(n))

#n=6(짝수)
#[1,1,1,1,1,1]-->6C0==1
#[1,1,1,1,2]-->5C1==5
#[1,1,2,2]-->4C2==6
#[2,2,2]-->3C0==1
#==>13

#def factorial(k): 팩토리얼 함수
#    fac=1
#    for k in range(1, k+1):
#        fac*=k
#    return fac


#return fac(int(a))/fac(int(b))/fac(int(a)-int(b)) 파트에서 하도많은 분할로 인해 에러
