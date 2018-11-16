#실습문제 6번-1번


string=input('Enter string: ')
vowel=[]
consonant=[]

for i in string:
    if i in 'aeiou':
        vowel.append(i)
    else:
        consonant.append(i)

print('number of vowels: {}'.format(len(vowel)))
print('number of consonants: {}'.format(len(consonant)))
