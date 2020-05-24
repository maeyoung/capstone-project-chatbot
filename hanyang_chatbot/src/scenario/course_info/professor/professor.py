import pandas as pd

DATA_IN_PATH = '/Users/maeyoung/capstone-project-chatbot/hanyang_chatbot/src/data/'

def course_professor(entity):
    # get_course_info_entity에서 추출한 entity를 사용해서 답변할 문장 만들기
    # ex) [['응용유기공업화학', '공업수학', '이정규'], ['SUBJECT', 'SUBJECT', 'PROFESSOR']]

    keyword = entity[0]
    tag = entity[1]
    subject = [] # 답변할 특정 강의명 
    department = []

    info_data = pd.read_csv(DATA_IN_PATH + 'course_info.csv', keep_default_na=False, index_col=0)

    # tag에 따라서 강의명과 답변할 강의정보 키워드 분리
    for k in zip(keyword, tag):
#         print(k)
        if 'SUBJECT' in k[1]:
            subject.append(k[0])
        elif 'DEPARTMENT' in k[1]:    # 답변할 강의의 특징 
            department.append(k[0])
            
    num = 0 

    # 학부가 같은데 교수님이 여러명 있는 경우 고려해야함 
    # 학부가 다 똑같은면 그냥 이 학부에서 리스트로 구성된 교수님이름 나열해주고 이렇게 있다고 보여주면 될듯 
    # OK

    for course_name in subject:
        
        pre_info = info_data[info_data['교과목명'] == course_name] # 한과목씩 과목정보를 불러옴
#         print(len(pre_info))

        print(department)
        
        if len(department) > 0:
            pre_info = pre_info[pre_info['설강학과'] == department[0]]

        else:
            depart = list(pre_info['설강학과'])
            depart = list(set(depart))

            if len(depart) > 1:
                print('땡땡봇 : ' + '어떤 과(학부)의 교수님명을 알고싶으신가요?')
                print(depart)
                print('Answer : ', sep = '', end='')
                input_department = input()
                pre_info = pre_info[pre_info['설강학과'].str.contains(input_department)]



        professor = list(pre_info['교강사'])
        professor = list(set(professor))

        result = ''
        for i in range(len(professor)):
            if i == (len(professor)-1):
                result += professor[i]
            else:
                result += professor[i] + ', '


        return "\"" + course_name + "\" 과목의 교강사는 " + result + " 교수님 입니다."
    
        # return professor
        

# intent 여러개로 나누고 거기에 맞는 시나리오 작성하기 