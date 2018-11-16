#Hackkerranks medium 'encryption' solve2

def encryption(s):
    from math import sqrt
    L=''
    M=''
    for i in s:
        if i!=' ':
            L+=i #L은 s에서 띄어쓰기 제거한 리스트

    row=int(sqrt(len(L))) #문장 수,3
    col=int(sqrt(len(L)))+1 #글자 칸수, 4
    
    for r in range(0, row):
        M+=str(L[0+col*r:col+col*r])+' ' #M은 columns의 개수에 맞춰서 잘라낸 리스트의 집합
    M=M.split()
    return M
    
            
    

    
#main

#s='if man was meant to stay on the ground god would have given us roots'
#s='feed the dog'
s='chill out'
print(encryption(s))       

'''feedthedog

feed
thed
og

fto ehg ee dd

s[0]+s[4]+s[8]+' '+s[1]+s[5]+s[9]+' '+s[2]+s[6]+' '+s[3]+s[7]
(0,4,8)+(1,5,9)+(2,6)+(3,7)'''
