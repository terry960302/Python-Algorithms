#프로그래머스 레벨3 '2xn 타일링' 풀기

def solution(n):
    if n%2!=0: #n이 홀수일 경우
        a=1
        if n==1:
            answer = a
        else:
            for i in range(1, int((n+1)/2)):
                a+=(2*i)
            answer = a
    else: #n이 짝수일 경우
        b=2
        if n==2:
            answer = b
        else:
            for j in range(1, int(n/2)):
                b+=((2*j)+1)
            answer = b
            
    return answer%1000000007
#main

n=int(input('n: '))
print(solution(n))
