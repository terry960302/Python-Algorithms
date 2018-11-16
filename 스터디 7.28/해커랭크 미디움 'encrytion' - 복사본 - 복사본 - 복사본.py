#Hackkerranks medium 'encryption' solve4

def encryption(s):
    from math import sqrt, ceil, floor
    #가장 먼저 할 일은 s를 공백없게 만들고 루트 구하기
    spacex=''
    for i in s:
        if ' ' != i:
            spacex+=i
    root=int(ceil(sqrt(len(spacex)))) #row 곱하기 column이 문자열의 전체길이를 넘어야하므로
    # 이어진 spacex에서 바로 답을 구하기
    answer=''
    for j in range(0, root): #0~6
        answer+=str(spacex[j::root])+' '#root만큼 건너뛰어서 글자를 산출
    return answer
    
    
    

    
#main

#s='if man was meant to stay on the ground god would have given us roots'
s='feed the dog'
#s='chill out'
#s='iffactsdontfittotheorychangethefacts'    
print(encryption(s))       


