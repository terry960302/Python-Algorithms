#프로그래머스 레벨3 '최고의 집합' 풀기4

def solution(n, s):
    from itertools import combinations as com

    L=[i for i in range(1, s+1)]
    M=[]
    if (n*(n+1))/2 > s: #1,2,3...,n의 합보다 s가 작다면
        return [-1]
    else:
        for j in com(L,n):
            if sum(j)==s:
                M.append(j)
    return list(M[-1])
            
#main

n=4 #원소의 개수
s=45 #분할하려는 수
print(solution(n,s)) #[4,5]


# 나열을 해보았을 때 앞에 숫자가 가장 크고(L[0]=max) 차례대로 나열되었을 경우 곱이 가장 큼


#10점인건 변함없으나 [-1]이 나오는 경우에 대해서 제대로 파악함.

#1,2,3 ->6
#1,2,3,4 -> 10
#1,2,3,4,5 -> 15
#1~6 -> 21
#[1,2,3,4,5,6,7] -> 28 #28일경우 최대로 만들수도 있는칸은 7칸임
