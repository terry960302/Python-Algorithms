#프로그래머스 레벨3 '최고의 집합' 풀기2

from itertools import combinations as com

def solution(n, s):
    L=[]
    M=[]
    if n>=s:
        return [-1]
    else:
        for i in range(1,s+1):
            L.append(i)
        for j in com(L,n):  #1부터 n까지 들어있는 리스트에서 sCn을 이용해서 그 중에 리스트의 합이 s인 것만 추출해서 M에 저장한다. 
            if sum(j)==s:
                M.append(j) #M은 s의 합으로 이루어진 원소가 n개 들어있는 조합들
        return list(M[-1])  #M의 원소들 중 맨마지막에 있는 원소의 총 곱이 가장 큼
            
#main

n=3 #원소의 개수
s=100 #분할하려는 수
print(solution(n,s)) #[4,5]


# 이 식은 단순히 n이 2일 경우만 생각해서
#i와 j 두개의 미지수만 두고 만들었으므로 실패
#n의 범위는 20이하의 자연수인 거 명심하셈.



#이것도 10점....n까지 고려했는데도 시간초과 때문에 다 틀림
