#실습문제 9번-1번


def encrypt(msg, code):
    k=''
    for i in msg:
        if i in code:
            k+=code[i]
    return k

# main

crypt_code = {'a':'g', 'b':'r', 'c':'q', 'd':'i', 'e':'u', 'f':'e', 'g':'w',
              'h':'n', 'i':'d', 'j':'l', 'k':'v', 'l':'t', 'm':'f', 'n':'s',
              'o':'o', 'p':'a', 'q':'k', 'r':'x', 's':'m', 't':'p', 'u':'y',
              'v':'b', 'w':'j', 'x':'z', 'y':'c', 'z':'h'}

plain_msg = input('Enter plain text : ')

encrypt_msg = encrypt(plain_msg, crypt_code)

print('crypted message :', encrypt_msg)
