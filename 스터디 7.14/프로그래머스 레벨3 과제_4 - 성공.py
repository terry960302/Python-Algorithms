#프로그래머스 레벨3 '2xn 타일링' 풀기

def solution(n):
    if n<2:         #피보나치가 1,1부터 시작하기 때문에 1을 반환한다.
        return 1

    a,b=0,1 
    for i in range(n):   #n이 자연수이기만 하면
        a,b = b,a+b     #0,1 다음엔 1,1 다음엔 1,2 다음엔 2,3 등등.....피보나치 수열의 특성

    return b%1000000007  #b가 앞에 두 수를 더한 값이기 때문에(b=a+b)

#main

n=int(input('n: '))
print(solution(n))


