import pandas as pd

DATA_IN_PATH = '/Users/jungyoon/Desktop/nlp/capstone-project-chatbot-master/hanyang_chatbot/src/data/'

def course_professor_info(entity):
    # get_course_info_entity에서 추출한 entity를 사용해서 답변할 문장 만들기
    # ex) [['응용유기공업화학', '공업수학', '이정규'], ['SUBJECT', 'SUBJECT', 'PROFESSOR']]

    keyword = entity[0]
    tag = entity[1]
    subject = [] # 답변할 특정 강의명
    quest = []

    info_data = pd.read_csv(DATA_IN_PATH + 'course_info.csv', keep_default_na=False, index_col=0)

    # tag에 따라서 강의명과 답변할 강의정보 키워드 분리
    for k in zip(keyword, tag):
#         print(k)
        if 'SUBJECT' in k[1]:
            subject.append(k[0])
        else:    # 답변할 강의의 특징
            quest.append(k[0])

    num = 0
    for course_name in subject:
#         if num == 0:
#             pre_info = info_data[info_data['교과목명'].str.contains(course_name)]
#             num += 1
#         else:
#             pre_info = pre_info.append(info_data[info_data['교과목명'].str.contains(course_name)])
        pre_info = info_data[info_data['교과목명'].str.contains(course_name)] # 한과목씩 과목정보를 불러옴
#         print(len(pre_info))
        if len(pre_info) > 1:
            print('땡땡봇 : ' + '어떤 과(학부)의 과목정보를 알고싶으신가요?')
#             print(pre_info['설강학과'])
            print('Answer : ', sep = '', end='')
            department = input()
            pre_info = pre_info[pre_info['권장학과'].str.contains(department)]


        professor = pre_info['교강사']

        return "\"" + course_name + "\" 과목의 교강사는 " + professor + " 교수님 입니다."

        # return professor
