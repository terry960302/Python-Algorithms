name='bill gates'
len(name) #len은 내장함수/ 문자열.____( ) =문자열 메소드(__에는 함수가 들어감.)
name.upper() #upper=모두 대문자/ lower=모두 소문자/capitalize=맨앞에것만 대문자고 나머지는 소문자/ title= 각 어절의 첫번째 문자만 대문자이고 나머지는 소문자로 만듬./is_____=t or f판별/ count=특정 문자열이 몇개 있는지 확인/ find=특정문자열이 몇번째 인덱스에 있는지 알려줌./
name.join() # ()에는 문자열로 구성된 리스트가 들어가야함.(리스트=[a,b,c]), join은 리스트안에 문자열들을 묶어라
name.split() #문자열을 ()속에 있는 것으로  리스트로 나눠라.

text= 'I got {} you got {}'#'____'.format(_____)에서 ''안에 {}이 두개가 나올 경우 ()에도 문자열이 두개가 와야함.(서로 대체하는 관계이기 때문)
text.format('apple', 'orange') #{}에다가 ()안에 쓴 내용이 들어감.
print('I got {} you got {}'.format('apple', 'orange'))#print를 적어야출력이 됨.
text= 'I got {1} you got {2}, he got {0}, she got {1}'
text.format(80, 90, 100) # I got 90, you got 100, he got 80, she got 90이 출력이 되는데 format에서 (0,1,2)순서로 출력이 되는것.

text='I got {:4d} you got {:10d}'
text format(85, 87)# 'I got ____85 you got __________87'
# '_____{:5.2f}___'.format(92.375) =다섯칸 잡아서 소수 두번째자리까지  표현하고 그 이상은 반올림.
#input('Enter x: ')에서 x에 대입되는 수는 문자열로 인식되기 때문에 계산이 따로 안됨.(그래서 앞에 int나 float을 붙어야 계산가능)
