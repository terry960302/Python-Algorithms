#중국어문화학과 2017650009 김태완

def make_dict(word):
    D={}
    for w in word:
        if w not in D:
            D[w]=1
        else:
            D[w]+=1
    return D
#main
word1 = input('word1 : ')
word2 = input('word2 : ')
D1 = make_dict(word1)
D2 = make_dict(word2)

if D1==D2:
   print('{} and {} are anagrams.'.format(word1, word2))
else:
    print('{} and {} are not anagrams.'.format(word1, word2))
