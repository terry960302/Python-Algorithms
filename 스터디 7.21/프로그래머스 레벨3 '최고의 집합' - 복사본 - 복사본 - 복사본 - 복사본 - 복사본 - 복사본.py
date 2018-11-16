#프로그래머스 레벨3 '최고의 집합' 풀기4

def solution(n, s):
    if n>s:
        return [-1]
    L = [s//n for i in range(n)]
    add = s-s//n*n
    while add>0:
        for i in range(n):
            if add>0:
                L[i]+=1
                add -= 1
            else:
                break
    return sorted(L)
                            
            
#main

n=10 #원소의 개수
s=10056 #분할하려는 수
print(solution(n,s)) #[4,5]


# 나열을 해보았을 때 앞에 숫자가 가장 크고(L[0]=max) 차례대로 나열되었을 경우 곱이 가장 큼


#
