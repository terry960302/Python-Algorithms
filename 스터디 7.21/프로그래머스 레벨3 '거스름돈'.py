#프로그래머스 레벨3 '거스름돈' 풀기1

def solution(n, money):
    count=0
    for a in range(0,n+1):
        for b in range(0, n+1):
            for c in range(0, n+1):
                if 1*a+2*b+5*c==n:
                    print (a,b,c)
                    count+=1
    return count
        
#동전의 개수가 3개일때만 한정, 암튼 대강 이런 식으로 문제 풀이

    
#main

n=5
money=[1,2,5]
print(solution(n, money))

[1,1,1,1,1]
[1,1,1,2]
[1,2,2]
[5]


7, [1,2,3]

[1,1,1,1,1,1,1]
[1,1,1,1,1,2]
[1,1,1,1,3]
[1,1,1,2,2]
[1,1,2,3]
[2,2,3]
