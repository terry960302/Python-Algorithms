age = int(input('Enter age: '))
price = int(input('Enter price: '))

if age < 18 or age >= 70:
    price=price*0.8
elif 60 <= age < 70:# 또다른 if를 쓰려면 elif로 하고 else안적어도됨.
    price=price*0.85
    
print('You should pay {: .2f}won.'.format(price))
