import json
import pandas as pd

f = open('./guess.json','r')
data = json.load(f)
data_rev = {}
fout2 = open('guess.csv','w')
for k_,v_ in data.items():
    tot = 0
    for ch in k_:
        if ch.isalpha():
            tot+=1
    if v_ not in data_rev.keys():
         data_rev[v_] = tot/5+1
    else:
        data_rev[v_] = min(data_rev[v_],tot/5+1)
    if v_ == 'favor':
        print(k_)
        print(data_rev['favor'])
fout2.write('word,score\n')
for k_,v_ in data_rev.items():
    fout2.write('{},{}\n'.format(k_,v_))

f.close()
f = open('./salet.txt','r')
data_rev2 = {}
fout2 = open('guess2.csv','w')
for line in f.readlines():
    word = line.split(',')
    word = [_.strip() for _ in word]
    if word[-1] not in data_rev2:
        data_rev2[word[-1]] = len(word)
    else:
        data_rev2[word[-1]] = min(data_rev2[word[-1]],len(word))
fout2.write('word,score\n')
for k_,v_ in data_rev2.items():
    fout2.write('{},{}\n'.format(k_,v_))


f.close()
fout = open('score.csv','w')
fout.write('word,score\n')
df = pd.read_excel('../data.xlsx')
for i in range(len(df)):
    tot = data_rev[df.word.iloc[i]]
    fout.write('{},{}\n'.format(df.word.iloc[i],tot))

fout = open('score2.csv','w')
fout.write('word,score\n')
for i in range(len(df)):
    tot = data_rev2[df.word.iloc[i]]
    fout.write('{},{}\n'.format(df.word.iloc[i],tot))