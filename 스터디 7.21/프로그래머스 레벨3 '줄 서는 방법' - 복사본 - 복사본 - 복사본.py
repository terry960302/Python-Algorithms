#프로그래머스 레벨3 '줄 서는 방법' 풀기4

def solution(n, k):
    L=[i for i in range(1,n+1)]    
    if n==1:
        return L
    else:
        result=[]
        for i in L:
            b = L.copy()
            b.remove(i)
    
#main

n=3 #몇까지 나열할 것인가
k=5 #몇 번째 순열인지 
print(solution(n, k))#[3,1,2]



[1,2,3,4]
[1,2,4,3]

[1,3,2,4]
[1,3,4,2]

[1,4,2,3]
[1,4,3,2]
