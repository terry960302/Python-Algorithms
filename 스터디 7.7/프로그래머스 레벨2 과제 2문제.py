
#프로그래머스 레벨2 피보나치 수

def solution(n):
    L=[0,1]
    #여기서부터
    if n==2:
        L.append(L[0]+L[1])
    elif n==3:
        L.append(L[0]+L[1])
        L.append(L[1]+L[2])
    elif n==4:
        L.append(L[0]+L[1])
        L.append(L[1]+L[2])
        L.append(L[2]+L[3])
    elif n==5:
        L.append(L[0]+L[1])
        L.append(L[1]+L[2])
        L.append(L[2]+L[3])
        L.append(L[3]+L[4])
    #여기까지는 예시나열
    if 2 <= n <= 100000:
        for i in range(n):
            L.append(L[i]+L[i+1])
    return L[n]


# 프로그래머스 레벨2 최댓값과 최솟값

def solution(s):
    s=s.split()
    L=[]
    for i in s:
        L.append(int(i)) #string인 숫자를 정수로 바꾸기 위함
    return str(min(L))+' '+str(max(L)) #최솟값과 최댓값을 다시 string으로 표현해서 출력하기 위함

         
