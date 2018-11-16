#프로그래머스 레벨3 '최고의 집합' 풀기3

from itertools import combinations as com

def solution(n, s):
    if n>=s:
        return [-1]
    else:
        L=[i for i in range(1, s+1)]
        for j in com(L,n):  #1부터 n까지 들어있는 리스트에서 sCn을 이용해서 그 중에 리스트의 합이 s인 것만 추출해서 M에 저장한다. 
            if sum(j)==s:
                answer=list(j)
    return answer #if문 바깥에서 값을 반환하면 맨마지막 원소가 반환되는 원리 이용

#main

n=3 #원소의 개수
s=10 #분할하려는 수
print(solution(n,s)) #[4,5]


# 이 식은 단순히 n이 2일 경우만 생각해서
#i와 j 두개의 미지수만 두고 만들었으므로 실패
#n의 범위는 20이하의 자연수인 거 명심하셈.



#이것도 10점....굳이 리스트 추가로 안만들었는데도 시간초과 때문에 다 틀림
