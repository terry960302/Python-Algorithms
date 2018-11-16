#실습문제 6번-2번


words = ['hundred', 'school', 'theater', 'python']

longest_w=words[0]

for w in words:
    if len(longest_w)<len(w):
        longest_w=w

print('longest word: {}'.format(longest_w))
print('length: {}'.format(len(longest_w)))
