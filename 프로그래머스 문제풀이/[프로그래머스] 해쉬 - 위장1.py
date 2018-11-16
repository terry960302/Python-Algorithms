#프로그래머스 레벨2 '위장'풀이1

"""
<문제접근>
1. 우선 a라는 종류가 있고 b라는 종류가 있으면 
2. 총 개수 = a개수 + b개수 + a*b
3. 고로 사전을 이용해서 종류 분류만 잘하면 그만.
4. 다시금 설명하자면 종류간의 합집합이라고 보면 된다. 
"""

def solution(clothes):
    D={}
    for i in range(0, len(clothes)):
        D.setdefault(clothes[i][1], []).append(clothes[i][0]) #여기서 의상종류를 key로, value는 리스트로 처리해서 동일한 의상종류에 대해 추가한다.
    sum = 1
    for j in D.values():
        sum *= len(j)
    if len(D.keys()) == 1: #종류가 하나일땐 걍 옷 몇가지만 있는지 알면 됨
        return len(clothes)
    else: #옷이 여러가지면 가짓수를 곱해서 더해야 함.
        return sum + len(clothes)

#main

clothes = [["yellow hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green turban", "headgear"]]
print(solution(clothes))
