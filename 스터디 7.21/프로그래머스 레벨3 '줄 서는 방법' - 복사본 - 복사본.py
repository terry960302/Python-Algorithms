#프로그래머스 레벨3 '줄 서는 방법' 풀기3

from itertools import permutations as per

def solution(n, k):
    L=[i for i in range(1,n+1)]    
    count=0
    for j in per(L):
        count+=1
        if count==k:
            return list(j)
    
#main

n=3 #칸수
k=5 #전체 사람 수 
print(solution(n, k))#[3,1,2]




