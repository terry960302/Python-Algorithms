#Hackkerranks medium 'encryption' solve3

def encryption(s):
    from math import sqrt, pow
    #가장 먼저 할 일은 s를 공백없게 만들고 루트 구하기
    spacex=''
    for i in s:
        if ' ' != i:
            spacex+=i
    root=int(sqrt(len(spacex)))+1 #7
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


