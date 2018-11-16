#중국어문화학과 2017650009 김태완

def count_larger_than_n(L, n):
    c=[]
    for i in L:
        if i>=n:
            c.append(i)
    return len(c)
 
#main
    
L = [22, 80, 50, 43, 19, 2, 78, 90, 15]
print('L :', L)
n = int(input('Enter n : '))
count = count_larger_than_n(L, n)
print('There are {} numbers larger than {} in L.'.format(count, n))
