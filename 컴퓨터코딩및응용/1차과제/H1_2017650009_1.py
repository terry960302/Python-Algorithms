#중국어문화학과 2017650009 김태완

a= input('Enter string:')# 먼저 '나라:언어' 입력


if a.count(':')!=1:#':'의 수가 1개가 아니면 문장출력
    print("Need just one ':'")
else:
    b, c=a.split(':')#':'의 수가 1개면 ':'기준으로 나눠서 저장
    d=b.capitalize()#나라 맨앞글자 대문자화
    e=c.capitalize()#언어 맨앞글자 대문자화
    print('In {}, people speak {}.'.format(d, e))#포맷으로 출력
