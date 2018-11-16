#프로그래머스 레벨3 '거스름돈' 풀기1

def solution(n, money):
    sum=0
    if 1 in money:
        for i in money:
            if n//i==n:
                n//i=1
            sum+=n//i
        return sum
        
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


