#추가문제 2번

word=input('Enter word: ')
c=input('Enter one character: ')
a=0

while a<=len(word): #입력된 단어의 음절 수까지 반복문
    a+=1           #한 음절씩 오르쪽으로 이동
    if c==word[a]:
        print('count: {}'.format(a))

    #단어를 먼저입력받고 문자열순서대로 왼->오 순서로 반복문 돌림.
    #반복문이 돌 동안 그 문자에 해당하는 부분  출력함.
    #그 문자의 개수 출력
    
