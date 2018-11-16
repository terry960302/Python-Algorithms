#실습문제 8번-1번

def isordered(a,b,c):
    if a<=b<=c:
        k=True
    else:
        k=False
        
    return k

#main

x=int(input('Enter x: '))
y=int(input('Enter y: '))
z=int(input('Enter z: '))

if isordered(x, y, z)==True:
    print('({},{},{}) is ordered.'.format(x,y,z))
else:
    print('({},{},{}) is not ordered.'.format(x,y,z))
