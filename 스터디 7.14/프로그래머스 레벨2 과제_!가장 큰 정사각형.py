#프로그래머스 레벨2 '가장 큰 정사각형 찾기'

def solution(board):
    sum=0
    L=[]
    for m in range(len(board)-1): #위아래로 이동/ m=0,1,2,3
        for n in range(0,4): #옆으로 이동/ n은 각 원소
            if (board[m][n],board[m][n+1],board[m+1][n], board[m+1][n+1])==(1,1,1,1): #변이 2인 정사각형
                sum+=1
    return sum



#main

board= [[0,1,1,1], [1,1,1,1], [1,1,1,1], [0,0,1,0]]
print(solution(board))
