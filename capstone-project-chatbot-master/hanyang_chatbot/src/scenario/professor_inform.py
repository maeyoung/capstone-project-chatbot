import pandas as pd

DATA_IN_PATH = '/Users/jungyoon/Desktop/nlp/capstone-project-chatbot-master/hanyang_chatbot/src/data/'

# 종성 체크
def checkTrait(c):
    return (int((ord(c) - 0xAC00) % 28) != 0)

# 조사
def setJosa(inform):
    if checkTrait(inform[-1]) == True:
        josa = '은'
    else:
        josa = '는'
    return josa

# 정보 프린트
def print_inform(search_list):
    print(search_list['교강사명']+' 교수님의 정보는 다음과 같습니다.')
    for inform in search_list.columns:
        if search_list[inform] != '':
            return inform+' : '+search_list[inform]

# 학부 선택
def find_department(search_list):
    print('어떤 학과의 교수님 정보를 원하시나요?')
    print(search_list['학부'])
    department = input()
    if department in list(search_list['학부']):
        find_list = search_list[search_list['학부'].str.contains(department)]
        return find_list
    else:
        print('찾는 학부가 없습니다.')
        return

# 출력
def print_quest(search_list, quest):
    if list(search_list[quest])[0] == '':
        return quest+' 정보가 없습니다.'
    else:
        josa = setJosa(quest)
        return search_list['학부']+' '+search_list['교강사명']+' 교수님의 '+quest+josa+' '+search_list[quest]+'입니다.'
    
def professor_inform(entity):
    keyword = entity[0]
    tag = entity[1]
    prof = ''
    quest = ''

    info_data = pd.read_csv(DATA_IN_PATH+'prof_info.csv', keep_default_na=False)
    for k in zip(keyword, tag):
        if 'PROFESSOR' in k[1]:
            prof = k[0]
        if 'INFORM' in k[1]:
            quest = k[0]
    if prof == '' or quest == '':
        return '정보가 없습니다ㅠㅠ'
    else:
        search_list = info_data[info_data['교강사명'].str.contains(prof)]
        if quest == '정보':
            if len(search_list) >= 2:
                search_list = find_department(search_list)
            return print_inform(search_list)
        else:
            if quest == '메일':
                quest = '이메일'
            elif quest == '전화':
                quest = '연락처'
            if len(search_list) >= 2:
                search_list = find_department(search_list)
                return print_quest(search_list, quest)
            else:
                return print_quest(search_list, quest)