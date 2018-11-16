#실습문제 9번-2번

def CtoF(c):
    f=(9/5*c)+32
    return f

def FtoC(f):
    c=(f-32)*5/9
    return c

#main

choice=input('선택 ---> ')

if choice=='c' or choice=='C':
    C=int(input('섭씨 온도를 입력하십시오: '))
    print('섭씨 {:5.2f}도는 화씨 {:5.2f}도입니다.'.format(C, CtoF(C)))
elif choice=='f' or choice=='F':
    F=int(input('화씨 온도를 입력하십시오: '))
    print('화씨 {:5.2f}도는 섭씨 {:5.2f}도입니다.'.format(F, FtoC(F)))
else:
    print('잘못된 입력입니다.')
