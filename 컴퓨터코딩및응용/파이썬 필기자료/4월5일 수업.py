print('hello world') #while반복문 : while '조건식:' ~else(없을 수도있음):

a=1 #[1부터 5까지 출력], 시작점
while a<= 5: #5번 반복해라
      print(a) # a를 반복출력한다.
      a+=1  #1씩 증가한다, 설정안해놓으면 무한루프(얼마나 증가시킬것인가)

a=1 #[1부터 10까지의 합], 시작점
sum=0 #sum은 0부터 시작
while a<=10:
      sum+=a #a를 sum에다가 더해준다. (sum=sum+a)
      a+=1 #a를 1증가시킴.
print('sum:', sum)
sum(range(11))

a=2 #[1부터 10까지 짝수의 합]
sum=0
while a<=10:
      sum+=a
      a+=2   #2씩 증가
print('sum:', sum)

sum=0
a= int(input('숫자를 입력하세요: '))
while a<=5:
      sum+=a
print('sum:', sum)

#[입력한 숫자를 5번 받아서 다 더하는 식]
a=1
count=int(input('루프돌릴 횟수를 입력하세요: '))
total=0
while a<=5:
      n=int(input('숫자를 입력하세요: '))
      total+=n
      a+=1
print('total : {}'.format(total))

#[break]: 루프안에서만 사용가능, 루프를 끝내게함.
#무한루프
a=1
while True: #계속 참-무한루프
      print(a)
      if a==5 : break #a가 5일때 무한루프 중지
      a+=1
#while 조건식이 false가 나왔을때 만약 밑에 else가 있으면 while건너뛰고 else실행, break를 걸었는데 밑에 else가 있으면 걍 break때문에 else도 무시.
