#hackerranks medium 'The grid search' 풀기1

def solution(G,P):
    if len(G[0]) < len(P[0]): #P의 길이가 더 길면 그리드G 안에 들어갈 수 없음
        return 'No'
    else:
        index_1=[]#r이 들어가있는 R이 연속적인지
        index_2=[]#속해있는 r의 인덱스 파악(시작점 같은지)
        for r in P:
            for R in G:
                if r in R:
                    index_1.append(G.index(R))
                    for i in range(0, len(R)):
                        for j in range(1, len(R)+1):
                            if R[i:j] == r:
                                index_2.append([i,j-1])
        
        for i in range(0, len(index_1)): #행이 연속적인지 파악
            first = index_1[0]
            first += 1
            if first != index_1[-1]:
                answer = 'No'
            else:
                #속한 r의 인덱스가 같은지 파악
                for a in index_2:
                    if index_2[0] != a:
                        answer = 'No'
                    else:
                        answer = 'Yes'
        return answer

#main

t= int(input('t : '))  #t는 테스트 케이스의 개수
for t_itr in range(t): #테스트 케이스 개수만큼 (그리드,패턴)을 생성하는 듯
        RC = input('RC: ').split()# 인풋 받은 걸 띄어쓰기 기준으로 나눠서 RC리스트에 저장

        R = int(RC[0]) #첫번째 줄에 처음이 줄의 수

        C = int(RC[1]) #첫번째 줄에 두번째가 열의 수

        G = []  #그리드는 모두 리스트에 저장되나 봄

        for _ in range(R): #줄의 수만큼 그리드 만들기
            G_item = input('G에 들어갈 수들: ') # G_item은 인풋으로 받아와서
            G.append(G_item) # 받아온 걸 그리드 리스트에 차곡차곡 넣어줌

        rc = input('rc : ').split() # 인풋 받은 걸 띄어쓰기 기준으로 나눠서 rc리스트에 저장

        r = int(rc[0]) #패턴을 나타내는 첫번째 줄에 처음은 줄

        c = int(rc[1]) #두번째는 열

        P = [] #패턴P라는 리스트 생성

        for _ in range(r): # 줄의 수만큼 패턴 만들기
            P_item = input('P에 들어갈 수들 : ') #인풋 받아온 걸 P_item에 저장
            P.append(P_item) #글고 패턴P에 차곡차곡 넣어줌.



#문제 설명
'''*인풋의 조건*
    첫번째 줄에는 t(테스트할 케이스가 t개)라는 수가 포함되어야하고, 각 t는 R과 C가 띄어쓰기
     나누어져 있으며, 그리드G에서 줄과 열을 나타낸다.
     R줄을 통해, C를 가진 각 문자열은 그리드G를 나타낸다.
     그 줄은 r과 c가 띄어쓰기로 나누어진 수를 지니며,
     그리드P의 줄과 열을 나타낸다.
     r줄을 통해, c를 지닌 각 문자열은 패턴 P를 나타낸다.
    *아웃풋의 조건*
     답은 패턴p가 그리드G에서 나타나는가에 따라
     항상 YES와 NO로만 이루어진다.'''
'''예시
    문제의 예시를 통해 보았을 경우, 2개의 테스트 대상이 있고,
    두번째 줄에 10 10은 그리트G의 줄과 열이 10개, 10개라는 소리,
    밑에 쭉 내려가다보면 3 4하고 밑에 좌라락 수가 있는데 이 패턴
    이 그리드 G에 있는지만 확인하면 장땡.'''
