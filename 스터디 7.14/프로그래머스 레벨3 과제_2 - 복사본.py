#프로그래머스 레벨3 '멀리뛰기' 문제

from itertools import combinations as com #조합 모듈

def combination(a,b):
    L=[]
    count=0
    for k in range(1, a+1): #a를 이용해서 [1,2,3,4,...a-2, a-1, a]의 리스트 만들기
        L.append(k)
    for c in com(L,b):
        count+=1
    return count

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
#[2,2,2]-->3C3==1
#==>13



# 이건 걍 시간이 너무 오래걸림
