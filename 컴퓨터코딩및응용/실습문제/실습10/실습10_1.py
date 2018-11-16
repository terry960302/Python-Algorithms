file=input('Enter file name: ')
word=input('Enter word to search: ')

f=open('wash_face.txt', 'r')
a=0
for line in f:
   if word in line:
       a+=1
       print('line {} - {}'.format(a, line.count(word)))

