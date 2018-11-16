n=int(input('Enter n: '))
a=0

while a<=n:#25를 넣었을때 그 아래 숫자 모두 차례대로 제곱근인지 판별, 존재하면 break걸고 출력      
      a+=1
      if n==a**2:
            print(n, 'is perfect square of',a)
            break
else:
      print(n,'is not perfect square number')

      #완료 

