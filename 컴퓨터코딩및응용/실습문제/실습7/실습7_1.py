#실습문제 7번-1번

ages = {}
ages['Alice'] = 23
ages['Paul'] = 25
ages['Peter'] = 19
ages['Karen'] = 40
ages['Andy'] = 25
ages['Cindy'] = 30
ages['David'] = 19
ages['Sally'] = 28
ages['Tom'] = 22
ages['Sue'] = 32
ages['Bob'] = 31

name=input('Enter name: ')

for n in ages:
    if n==name:
        print('{} is {} years old'.format(name, ages[name]))
if name not in ages:
    print('{} is not in the "age" dictionary.'.format(name))
