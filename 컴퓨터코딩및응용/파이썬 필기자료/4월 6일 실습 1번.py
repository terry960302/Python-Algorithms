n=int(input('Enter n: '))
a=1
while a<=n:#약수는 항상 입력하는 수보다 작다.
   if n%a==0:#n을 a로 나누었을 때 나머지가 0일때 a는 n의 약수
       print('{:3d}'.format(a), end=' ')#end는 약수를 가로배열
   a+=1#a를 1씩 차례대로 넣어서 하나도 건너뛰지 않도록.
print()
