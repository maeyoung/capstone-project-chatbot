import pandas as pd
import numpy as np

prof = pd.read_csv('professor.csv', header=None)
prof = list(prof[0])

inform = ['이메일', '전화번호', '연락처', '연구실']
please = ['', '알려줘', '알려줄래', '찾아줘', '찾아줄래', '알아?']

intent = [] # 질문 set
tent = [] # 의도
for i in range(len(prof)):
    for j in range(len(inform)):
        for k in range(len(please)):
            sentence = prof[i]+ ' 교수님 '+ inform[j] + ' ' + please[k]
            intent.append(sentence)
            if j == 0: # 이메일
                tent.append('교수이메일')
            elif j == 1 or j == 2: # 전화번호, 연락처
                tent.append('교수연락처')
            else: # 연구실
                tent.append('교수연구실')
for name in prof:
    sentence = name + ' 교수님 연구실 어디야?'
    intent.append(sentence)
    tent.append('교수연구실')
for name in prof:
    for i in range(3):
        sentence = name + ' 교수님 정보 ' + please[i]
        intent.append(sentence)
        tent.append('교수님정보') #?

intent.extend(tent) # len(intent) = 45684
arr_intent = np.array(intent)
arr_intent = arr_intent.reshape(-1, len(tent)) # len(tent) = 22932
arr_intent = arr_intent.transpose()

new_intent = pd.DataFrame(arr_intent)
new_intent.to_csv('train_intent.csv')