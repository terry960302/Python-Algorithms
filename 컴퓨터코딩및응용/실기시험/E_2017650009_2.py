#중국어문화학과 2017650009 김태완


#QUESTION 과 나머지를 구분해서 리스트를 따로 만들어서 all이라는 리스트에 넣는 과정

f = open('question.txt', 'r')
all = []
line = f.readline().strip() #첫문장을 공백없이 읽어들이기
while line == 'QUESTION': #퀘스쳔 나올때마다
    p = []                  #리스트 생성하고
    line = f.readline().strip()  #그다음줄부터 또 생성
    while line and line != 'QUESTION': #밑에 질문과 선지들의 경우
        p.append(line)              #p에다가 넣어버림
        line = f.readline().strip()  #넣고 나서 다시 파일불러옴
    all.append(p)           #최종적으로 그리고 p를 더 큰 리스트에 추가


#Q1같은거 만들기 
no = 1
for i in all:  #all에는 질문과 그 이외의 요소가 다 들어있음
    Q = 'Q'+str(no)+'.'
    print(Q, i[0]) #i[0]은 Q에 해당함
    for j in range(1,len(i)): #Q옆에 붙는 숫자 넣기
        print(j, '. ', i[j], sep='')#sep을 이용해서 Q와 숫자를 붙임
    print()
    no += 1
