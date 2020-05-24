import pandas as pd  

DATA_IN_PATH = '/Users/maeyoung/capstone-project-chatbot/hanyang_chatbot/src/data/'

# 학점

def course_time(entity):
    # get_course_info_entity에서 추출한 entity를 사용해서 답변할 문장 만들기
    # ex) [['응용유기공업화학', '공업수학', '이정규'], ['SUBJECT', 'SUBJECT', 'PROFESSOR']]

    keyword = entity[0]
    tag = entity[1]
    subject = [] # 답변할 특정 강의명 
    professor = []
    department = []

    info_data = pd.read_csv(DATA_IN_PATH + 'course_info.csv', keep_default_na=False, index_col=0)

    # tag에 따라서 강의명과 답변할 강의정보 키워드 분리
    for k in zip(keyword, tag):
#         print(k)
        if 'SUBJECT' in k[1]:
            subject.append(k[0])  # ['이산수학']
        elif 'PROFESSOR' in k[1]:    
            professor.append(k[0])   # ['이정규']
        else:
            department.append(k[0]) # ['컴퓨터공학과']
            
    num = 0       
    for course_name in subject:

        pre_info = info_data[info_data['교과목명'] == course_name] # 한과목씩 과목정보를 불러옴
#         print(len(pre_info))

        #print(len(professor))

        # 교수님 정보가 이미 있는 경우 정보가 여러개이면 설강학과를 또 선택하게 함 
        if len(professor) > 0:
            pre_info = pre_info[pre_info['교강사'].str.contains(professor[0])]

            if len(pre_info) > 1:
                print('궁금하냥 : ' + '어떤 과(학부)의 변경전 교과목명을 알고싶으신가요?')  
                print(pre_info['설강학과'])
                print('Answer : ', sep = '', end='')
                input_department = input()
                pre_info = pre_info[pre_info['설강학과'].str.contains(input_department)]

        # 학과 정보가 이미 있는 경우 걸러진 정보가 여러개일 경우 교수님 정보로 한번더 추림 
        if len(department) > 0:
            pre_info = pre_info[pre_info['설강학과'].str.contains(department[0])] 

            name = list(pre_info['교강사'])
            name = list(set(name))

            if len(name) > 1:
                print('궁금하냥 : 이중에서 어떤 교수님 수업에 대해 알고싶으신가요?') 
                print(name)
                # print(pre_info['교강사'])
                print('Answer : ', sep = '', end='')
                input_professor = input()
                pre_info = pre_info[pre_info['교강사'].str.contains(input_professor)]
        
        name = list(pre_info['설강학과'])
        name = list(set(name))

        if len(name) > 1:
            print('궁금하냥 : 이중에서 어떤 학부 수업에 대해 알고싶으신가요?') 
            print(name)
            # print(pre_info['교강사'])
            print('Answer : ', sep = '', end='')
            input_professor = input()
            pre_info = pre_info[pre_info['설강학과'].str.contains(input_professor)]
            
        # print(pre_info)

        theory = list(pre_info['강의'])[0]
        practice = list(pre_info['실습'])[0]

        
        return "\"" + course_name + "\" 과목은 강의 " + str(theory) + " 시간, 실습 " + str(practice) + " 시간으로 구성된 수업입니다."
        