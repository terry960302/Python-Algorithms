#프로그래머스 레벨4 '올바른 괄호의 갯수' 풀기1

def solution(s, n):
    a_s=abcdefghijklmnopqrstuvwxyz
    a_b=alphabet_s.upper()
    
    for i in s:
        if i == i.lower():
            if i in a_s:
                answer = a_s

#main

s="AB"
n= 1
print(solution(s,n))


