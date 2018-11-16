#중국어문화학과 2017650009 김태완
career=int(input('career: '))
wh=int(input('working hour: '))

if career>=36:
    a=wh*15000*0.985
    print('weekly salary: {:.2f}'.format(a))
elif 12 <= career < 36:
    b=wh*12000*0.985
    print('weekly salary: {:.2f}'.format(b))
elif career<12:
    c=wh*9000*0.985
    print('weekly salary: {:.2f}'.format(c))


