#프로그래머스 레벨3 '줄 서는 방법' 풀기2

from itertools import permutations as per

def solution(n, k):
    L=[]
    for i in range(1,n+1): #[1,2,3,...,n-1,n]리스트를 만들어서 퍼뮤테이션에 사용하려고
        L.append(i)
        
    count=0
    for j in per(L):
        count+=1
        if count==k:
            return list(j)

#main

n=3
k=5
print(solution(n, k))


#73.7 (다른건 다 맞았는데 효율성 테스트에서 썰림)
