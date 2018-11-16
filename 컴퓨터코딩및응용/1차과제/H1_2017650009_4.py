#중국어문화학과 2017650009 김태완

age= int(input('나이를 입력하세요: '))
height= int(input('키를 입력하세요: '))

if age >= 8 and height >= 120:
    print('입장하세요!!')
elif age >= 8 and height < 120:
    print('키가 120cm를 넘어야 입장 가능합니다.')
elif age < 8 and height >= 120:
    print('나이가 8세 이상이어야 입장 가능합니다.')
elif age < 8 and height < 120:
    print('나이가 8세 이상, 키가 120cm 이상이어야 입장 가능합니다.')
