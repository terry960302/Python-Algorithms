f=open('population.txt', 'r')

D={}
for line in f:
    line=line.split()
    density=int(line[1])/int(line[2])
    D[line[0]]=density

    if density>=1000:
        k='is very densely populated'
    elif density>=500:
        k='is densely populated'
    elif density>=300:
        k='is normally populated'
    elif density>=100:
        k='is sparsely populated'
    elif density<100:
        k='is very sparsely populated'
    print('{} {}'.format(line[0], k))
