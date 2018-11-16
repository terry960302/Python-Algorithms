#중국어문화학과 2017650009 김태완

def func(D):
    D={}
    for days in May:
        for name in May[days]:
            D[name]=[]
            for days in May:
                if name in May[days]:
                    D[name].append(days)
    return D

# main
May = {}
May[1] = ['Alice', 'Tom', 'David', 'Peter']
May[2] = ['Alice', 'Cindy', 'David', 'Eve', 'Peter']
May[3] = ['Mary', 'Tom', 'Bob', 'David', 'Jenny', 'Paul', 'Cindy']
May[4] = ['Cindy', 'David', 'Jenny', 'Bob', 'Tom']
May[5] = ['Alice', 'David', 'Eve', 'Paul', 'Bob']
May[6] = ['Cindy', 'David', 'Alice', 'Mary', 'Bob', 'Tom', 'Peter', 'Jenny']
May[7] = ['Peter', 'David', 'Tom']

result = func(May)

for name, days in result.items():
    print('{:7s} : {}'.format(name, days))
