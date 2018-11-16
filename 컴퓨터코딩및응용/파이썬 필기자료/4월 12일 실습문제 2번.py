n=int(input('Enter n: '))

while True:
      if n%2==0: #짝수이면
            print('You enter even number', n)
      elif n%2!=0: #홀수이면
            a=1
            while a<=n:#소수판단
                  n%a=0#a가 약수인지 판단
                  if a>1:
                        print(n,'is not a prime number')
                  else:
                        print(n, 'is  a prime number')

else n==0:
      break

#미완료 
