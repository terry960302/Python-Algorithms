#프로그래머스 레벨3 '야근지수' 풀이

#n에서 먼저 분할 시작

def division(a,b):
    L=[]
    for l in range(a+1):
        for m in range(a+1):
            for n in range(a+1):
                if l+m+n==a:
                    return [l,m,n]
def solution(n, works):
    sum=0
    m=[]
    for k in range(0, len(works)):
        works[k]=works[k]-division(n, len(works))[k]
    for i in range(0, len(works)):
        sum+=works[i]**2
        return works



#main

works=[100,3,3]
n=6

print(solution(n, works))

#각 원소의 범위가 works의 원소이하인걸 감안해서 만든 식
