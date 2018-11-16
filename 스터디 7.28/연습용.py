#연습용 


def solution(arr):

    D = {}#사전 만들기
    for i in range(len(arr)): #리스트의 원소 수만큼
        D[arr[i]] = i #키에는 원소를 넣고, 값에는 인덱스를 넣는다
        
    L = sorted(arr) #리스트를 오름차순한 것
    count = 0 #아마 횟수세기용일 듯
    
    for i in range(len(arr)): #또 리스트의 수만큼 
        if arr[i] != L[i]: #리스트의 원소가 오름차순한 리스트와 일치하지 않으면
            count +=1    #횟수를 늘린다.
            
            swap = D[ L[i] ] #오름차순한 리스트의 원소에 해당하는 m의 인덱스를 대입함.
            D[ arr[i] ] = D[ L[i]]  #m의 키에 해당하는 값에다가 그 m의 인덱스를 넣어버림.
            arr[i],arr[swap] = L[i],arr[i] #그렇게 자리바꾸기
    return count


#main

a=[2,1,3,5,4]
print(solution(a))








