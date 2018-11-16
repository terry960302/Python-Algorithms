#중국어문화학과 2017650009 김태완

score = {'Alice':[80, 90, 88],'Paul':[77, 92, 90],'David':[80, 70, 80],'Cindy':[80, 92, 95],'Tom':[85, 65, 70]}
key=list(score.keys())
value_list=[]
average={}

for v in score.values():
    va=sum(v)/3
    value_list.append(va)

for i in range(5):
    average[key[i]]=value_list[i]

for m,n in average.items():
    print('{:10}   {:5.2f}'.format(m,n))


