word=input('Input word to test anagram: ')
print()

def anagram(word):
    D={}
    for i in word:
        if i not in D:
            D[i]=1
        else:
            D[i]+=1
    return D

#main

f=open('word.txt', 'r')
a=0
for line in f:
    line=line[:-1] #뒤에 있는 \n 제거하기 위해서 [:-1]붙여서 대입
    if anagram(line)==anagram(word):
       print(line)
       a+=1
print('-'*15)
print('There are {} anagrams'.format(a))    
    

