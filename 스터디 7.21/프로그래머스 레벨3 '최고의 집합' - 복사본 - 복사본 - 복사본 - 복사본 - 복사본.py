#프로그래머스 레벨3 '최고의 집합' 풀기4

def solution(n, s):
    if (n*(n+1))/2 > s: #1,2,3...,n의 합보다 s가 작다면
        return [-1]
    else:
        if round(s/n)<=s/n: #최대 곱을 갖는 answer의 원소 시작점 구하기
            start=s//n-n//2
        else:
            start=s//n-(n//s-1)
        L=[i for i in range(0, n)] #start를 시작으로 1씩 오름차순 배열
        for j in range(0,n):
            L[j]+=start
        if sum(L)==s:
            return L
        else:
            L=L[::-1] #뒤에서부터 1씩 넣을려고
            for k in range(0, s-sum(L)):
                L[k]+=1
        return L[::-1]
                            
            
#main

n=10 #원소의 개수
s=10056 #분할하려는 수
print(solution(n,s)) #[4,5]


# 나열을 해보았을 때 앞에 숫자가 가장 크고(L[0]=max) 차례대로 나열되었을 경우 곱이 가장 큼


#
