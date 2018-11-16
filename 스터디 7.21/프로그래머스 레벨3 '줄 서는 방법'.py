#프로그래머스 레벨3 '줄 서는 방법' 풀기1

from itertools import permutations as per

def solution(n, k):
    L=[]
    M=[]
    for i in range(1,n+1):
        L.append(i)
    for j in per(L):
        M.append(list(j))
    return M[k-1]

#main

n=3
k=5
print(solution(n, k))


#63.2 (일반 테스트에서 2개 틀리고, 효율성 테스트에서 전사함)
