#중국어문화학과 2017650009 김태완

def differ_by_one_char(s1, s2):
    if len(s1)!=len(s2):
        a=False
    else:
        L=[]
        for m in s1:
            if m in s2:
                L.append(m)
                if len(L)==(len(s1)-1):
                    a=True
                else:
                    a=False
    return a
                
#main

word1 = input('Enter word1: ')
word2 = input('Enter word2: ')
W = (word1, word2)
if differ_by_one_char(word1, word2):
    print(W, ': differ by one character')
else:
    print(W, ':not differ by one character')
