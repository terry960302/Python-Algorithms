#중국어문화학과 2017650009 김태완
voca = ['python', 'c', 'c++', 'java', 'java', 'javascript', 'python', 'ruby',
        'swift', 'c', 'c', 'java', 'python', 'ruby', 'swift', 'cobol', 'cobol',
        'r', 'r', 'c', 'c', 'r', 'html', 'html', 'ruby']

voca_dict=dict.fromkeys(voca,0)
vlist=list(voca_dict.keys())
value=[]
for v in voca_dict.keys():
    value.append(voca.count(v))
for i in range(len(voca_dict)):
    voca_dict[vlist[i]]=value[i]
for m,n in voca_dict.items():
    print('{} - {} times'.format(m,n))

    
