import pandas as pd
#inputs = pd_read_csv('sub_sort.csv', header=None)
# 종성 받침 유무 체크
def checkTrait(c):
    return (int((ord(c) - 0xAC00) % 28) != 0)

last = []
for line in inputs[0]:
    if(checkTrait(line[-1]) == False):
        last.append('F')
    else:
        last.append('T')

lasts = pd.DataFrame(last)
#lasts.to_csv('last.csv')