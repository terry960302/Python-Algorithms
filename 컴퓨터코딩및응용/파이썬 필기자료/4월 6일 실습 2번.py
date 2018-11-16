n=int(input('Enter n: '))#횟수를 지정하시오.
print('-'*20)#밑줄 긋기

a=1 #a에는 1부터 대입.
while a<=n:
    data=int(input('Enter data: '))#data를 입력하시오
    if a==1:max_data=data#a가 1이었을 경우 max_data에 data를 대입.(가장 처음 대입한 값이 최대값이라고 규정)
    else:               #위의 경우가 아닐경우(다른 경우의 조건을 입력하고 싶을 때)
        if data>max_data: #만약 앞으로 입력할  데이터가 max_data(과거의 입력한 데이터)보다 클 경우
            max_data=data #최댓값은 출력될 데이터가 된다.
    a+=1#a는 1씩 차례대로 증가
print('-'*20)
print('max data: {}'.format(max_data))#입력한 데이터중에서 가장 큰 데이터를 출력하시오.
