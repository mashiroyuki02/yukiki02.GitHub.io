import os
fin = open('words.txt',mode='r')
fout = open('words5.txt',mode='w')

for word in fin.readlines():
    word = word.strip()
    if len(word)==5 and word.isalpha():
        fout.write('{}\n'.format(word.lower()))