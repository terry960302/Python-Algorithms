#중국어문화학과 2017650009 김태완

words = ['book', 'pencil', 'mirror', 'to', 'for', 'with',
         'cup', 'computer', 'chair', 'of', 'a', 'an', 'I',
         'desk', 'school', 'cat', 'lamp']
wl=[]
L=[]
wd={}

for i in range(len(words)):
    wl.append(len(words[i]))
    wl=dict.fromkeys(wl)
    wl=list(wl.keys())
    
for k in range(len(wl)):
    L.append([])
    for w in range(len(words)):
        if wl[k]==len(words[w]):
            L[k].append(words[w])
            wd[wl[k]]=L[k]

for m,n in wd.items():
    print('word list of length {}: {}'.format(m, n))
        

    
