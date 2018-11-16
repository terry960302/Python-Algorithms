#프로그래머스 레벨3 '최고의 집합' 풀기4

def solution(n, s):
    if n>=s:
        return [-1]  #예를 들어 n==s일 경우는 [1,1,1,1,....1]이 될수있는데 만약 n>s라면 자연수범위내에서 만들수가 없다.
    else:
        L=[]
        for i in range(0,n): #n의 개수만큼 몫을 집어넣기 위함        
            L.append(s//n)   #나눈 몫을 n의 수만큼 리스트에 넣는다.(나머지는 항상 몫보다 작다는 원리 이용하기 위해서)
        if s%n==0:           #만약 나머지가 없으면 그냥 반환하면 그만이지만
            return L
        else:    #나머지가 존재하게 되면 오름차순으로 만들어야하기 때문에 뒤에서부터 나머지를 1씩 쪼개서 더해준다.
            for k in range(0,s%n):
               L[k]+=1  #앞에서부터 1씩 더해준다음
            return L[::-1]  #뒤집어서 반환하면 끝!


#main

n=10 #원소의 개수
s=10056 #분할하려는 수
print(solution(n,s)) #[4,5]


# 나열을 해보았을 때 앞에 숫자가 가장 크고(L[0]=max) 차례대로 나열되었을 경우 곱이 가장 큼


#이것도 10점...이전 공식들은 그래도 다 시간초과에서 걸렸는데 이번엔 시간초과뿐만 아니라 효율성 검사에서 실패가 있는 걸 보면 이 식은 야매로 만든 거 같음.
