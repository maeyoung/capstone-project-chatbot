import pandas as pd
import numpy as np

prof = pd.read_csv('professor.csv', header=None)
prof = list(prof[0])

inform = ['','정보'] # For making 정보.csv
mail = ['메일', '이메일'] # For making 이메일.csv
phone = ['전화번호', '연락처'] # For making 연락처.csv
room = ['연구실'] # For making 연구실.csv
please = ['', '알려줘', '알려줄래', '찾아줘', '찾아줄래', '알아?']

question = [] # 질문 set
intent = [] # 의도
for i in range(len(prof)):
    for j in range(len(inform)): # 만들 때 바꾸기 -> inform / mail / phone / room
        for k in range(len(please)):
            sentence = prof[i]+ ' 교수님 '+ inform[j] + ' ' + please[k] # 만들 때 바꾸기 -> inform / mail / phone / room
            intent.append('정보') # 만들 때 바꾸기 -> 정보 / 이메일 / 연락처 / 연구실

# 연구실.csv 만들 때만 사용
for name in prof:
    sentence = name + ' 교수님 연구실 어디야?'
    question.append(sentence)
    tent.append('연구실')

question.extend(tent)
arr_intent = np.array(question)
arr_intent = arr_intent.reshape(-1, len(intent))
arr_intent = arr_intent.transpose()

new_intent = pd.DataFrame(arr_intent)
new_intent.to_csv('정보.csv') # 만들 때 바꾸기 -> 정보 / 이메일 / 연락처 / 연구실