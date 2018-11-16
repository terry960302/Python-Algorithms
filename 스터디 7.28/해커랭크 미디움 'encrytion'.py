#Hackkerranks medium 'encryption' solve

def encryption(s):
    from math import sqrt
    L=[]
    M=[]
    for i in s:
        if i!=' ':
            L.append(i) #L은 s에서 띄어쓰기 제거한 리스트

    row=int(sqrt(len(L))) #문장 수,3
    col=int(sqrt(len(L)))+1 #글자 칸수, 4

    for r in range(0, row):
        M.append(L[0+col*r:col+col*r]) #M은 columns의 개수에 맞춰서 잘라낸 리스트의 집합

    for k in range(0,col):
        answer=M[0][0]+M[1][0]+M[2][0]+' '+M[0][1]+M[1][1]+M[2][1]+' '+M[0][2]+M[1][2]+M[2][2]
    
    
    
    


#main

#s='if man was meant to stay on the ground god would have given us roots'
s='feed the dog'
print(encryption(s))       
