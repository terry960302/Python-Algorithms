#프로그래머스 레벨3 '최고의 집합' 풀기


def solution(n, s):
    L=[]
    M=[]
    if n>=s:
        return [-1]
    for i in range(1,s):
        for j in range(1,s):
            if i+j==s and i<=j:
                L.append([i,j])
                M.append(i*j)
    if M.count(max(M))>1:
        return [-1]
    else:
        return L[M.index(max(M))]


#main

n=2
s=9
print(solution(n,s)) #[4,5]


# 이 식은 단순히 n이 2일 경우만 생각해서
#i와 j 두개의 미지수만 두고 만들었으므로 실패
#n의 범위는 20이하의 자연수인 거 명심하셈.


#10점 ㅋㅋㅋ 걍 잘못 푼
