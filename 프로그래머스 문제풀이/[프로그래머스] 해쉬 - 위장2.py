#프로그래머스 레벨2 '위장'풀이2

"""
<문제접근>
1. 우선 a라는 종류가 있고 b라는 종류가 있으면 
2. 총 개수 =  2개씩 묶어서 곱을 구한다음 3개씩 묶어서 구하고 종류의 수까지 반복해준다.
3. 그리고 그렇게 묶음이 끝나면 종류 상관없이 원소의 총개수를 더하면 끝
4. 종류의 수는 key의 개수, key의 개수 만큼 1부터 key까지 반복문을 돌린다.
5. 
"""

def solution(clothes):
    
    allsum = len(clothes) #나중에 더할 것

    D={}
    for i in range(0, len(clothes)):
        D.setdefault(clothes[i][1], []).append(clothes[i][0]) #여기서 의상종류를 key로, value는 리스트로 처리해서 동일한 의상종류에 대해 추가한다.
    #setdefault는 말그대로 사전의 초기형태를 만들어준다는 의미이다.
        
   #그 다음엔 빠른 계산을 위해 value값을 원소의 개수로 바꿔준다.
    for j in D.keys():
        D[j] = len(D[j])

    #이제 2개씩 묶는거부터 시작해서 key의 개수만큼 반복할 것(2~len(key))
    
        
        

#main

clothes = [["yellow hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green turban", "headgear"]]
print(solution(clothes))
