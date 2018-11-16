#Hackkerranks medium 'encryption' solve3

def encryption(s):
    from math import sqrt
    #가장 먼저 할 일은 s를 공백없게 만들고 루트 구하기
    spacex=''
    for i in s:
        if ' ' !=i:
            spacex+=i
    root=int(sqrt(len(spacex)))+1 #3
    #그 다음은 root만큼 spacex를 나누기
    divide=''
    for j in range(1, (len(spacex)//root)+2): #(len(spacex)//root)+1은 나눴을 때 나오는 라인의 수
        divide += str(spacex[root*(j-1): root*j-1+1])+' '
    return divide
    
    
    

    
#main

#s='if man was meant to stay on the ground god would have given us roots'
s='feed the dog'
#s='chill out'
print(encryption(s))       

'''feedthedog

feed
thed
og

fto ehg ee dd

s[0]+s[4]+s[8]+' '+s[1]+s[5]+s[9]+' '+s[2]+s[6]+' '+s[3]+s[7]
(0,4,8)+(1,5,9)+(2,6)+(3,7)'''
