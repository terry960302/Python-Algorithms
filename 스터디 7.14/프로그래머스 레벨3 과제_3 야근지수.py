#프로그래머스 레벨3 '야근지수' 풀이

#works에서 분할 시작

def solution(n, works):
    L=[]
    answer=0
    a=sum(works)-n
    if a<=0:
        return answer
    else:
        b=a//len(works) #7//3 = 2
        for k in range(0,len(works)): #세칸에 각2씩 분배
            L.append(b)
            
        if a%len(works)!=0:  #a를 칸수로 나눴는데 나머지가 남으면 밑에 더해주는 과정이 추가적으로 필요  
            for i in range(0,a%len(works)): #7%3 = 1
                L[i]+=1
            
        for k in L:
            answer+=k**2
            
        return answer



#main

works=[4,4,3]
n=4

print(solution(n, works))
