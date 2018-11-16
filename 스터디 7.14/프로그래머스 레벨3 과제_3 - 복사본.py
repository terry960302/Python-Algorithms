#프로그래머스 레벨3 '야근지수' 풀이

#n에서 먼저 분할 시작

def solution(n, works):
    works=sorted(works)[::-1] # works를 내림차순 리스트로 변환
    answer = 0
    L = [] #n을 분할해서 만들 리스트
    if sum(works)-n<=0:
        return answer
    else:
        for i in range(0, len(works)):
            works[i]=works[i]-(n//len(works)) #n%len(works)=0일 경우 여기서 멈춤 
        
        if n%len(works)!=0:
            for k in range(0, n%len(works)):
                works[k]=works[k]-1 #works가 내림차순 이므로 앞에서부터 차례대로 1씩 빼줌(어차피 나머지는 칸수에 모두 1씩 분배가능함.나누고자 하는 수>나머지)
        
        for a in works:
            answer+=a**2
            
        return answer    



#main

works=[100,3,3]
n=6

print(solution(n, works))

#각 원소의 범위가 works의 원소이하인걸 감안해서 만든 식
