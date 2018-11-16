#중국어문화학과 2017650009 김태완

quantity= int(input('사용량을 입력하세요: '))
rating= int(input('등급을 입력하세요: '))

if rating==1:
    k=765
    spent= quantity*k
    allspent= spent+ (spent*0.1)
    print('세금: {:.2f}'.format(spent*0.1))
    print('총 사용 금액: {:.2f}'.format(allspent))
elif rating==2:
    k=577
    spent= quantity*k
    allspent= spent+ (spent*0.1)
    print('세금: {:.2f}'.format(spent*0.1))
    print('총 사용 금액: {:.2f}'.format(allspent))
elif rating==3:
    k=355
    spent= quantity*k
    allspent= spent+ (spent*0.1)
    print('세금: {:.2f}'.format(spent*0.1))
    print('총 사용 금액: {:.2f}'.format(allspent))
else:
    print(rating,'은(는) 없는 등급입니다.')

    

