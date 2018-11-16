#실습문제 7번-2

word=input('Enter one word: ')

for i in 'aeiou':
    vowel=dict.fromkeys(i, 0)

    for w in word:
        if w==i:
            vowel[i]+=1

    for m,n in vowel.items():
        print('vowel {}: {}'.format(m, n))
    

