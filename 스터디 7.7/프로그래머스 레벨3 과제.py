#프로그래머스 레벨3 가장 긴 펠린드롬

def solution(s):
    L=[]
    for i in range(len(s)):
        for k in range(1, len(s)+1): #k가 i보다 뒤에 있게 해서 문자열 뽑아내려고
            if s[i:k] == s[i:k][::-1]: #문자열 내에서 거꾸로 뒤집어도 같은 것을 뽑아내려고
                L.append(len(s[i:k])) #거꾸로 해도 같은 문자열의 길이를 리스트에 저장
    return max(L)   #리스트에 저장된 팰린드롬의 길이들 중에서 가장 긴 걸 반환



#main

s='abaaba'
print(solution(s))
