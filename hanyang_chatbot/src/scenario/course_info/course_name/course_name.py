import pandas as pd  

DATA_IN_PATH = '/Users/maeyoung/capstone-project-chatbot/hanyang_chatbot/src/data/'

# 강목명

def course_name(entity):
    # get_course_info_entity에서 추출한 entity를 사용해서 답변할 문장 만들기
    # ex) [['응용유기공업화학', '공업수학', '이정규'], ['SUBJECT', 'SUBJECT', 'PROFESSOR']]

    keyword = entity[0]
    tag = entity[1]
    subject = [] # 답변할 특정 강의명 
    professor = []
    department = []
    evaluation =[]
    classification = []
    field = []
    pbl = []
    english = []
    grade_class = []

    pre_info = pd.read_csv(DATA_IN_PATH + 'course_info.csv', keep_default_na=False, index_col=0)

    # tag에 따라서 강의명과 답변할 강의정보 키워드 분리
    for k in zip(keyword, tag):
#         print(k)
        if 'PROFESSOR' in k[1]:    
            professor.append(k[0])   # ['이정규']
        elif 'DEPARTMENT' in k[1]:
            department.append(k[0]) # ['컴퓨터공학과']
        elif 'EVALUATION' in k[1]:
            evaluation.append(k[0])
        elif 'CLASSIFICATION' in k[1]:
            classification.append(k[0])
        elif 'FIELD' in k[1]:
            field.append(k[0])
        elif 'PBL' in k[1]:
            pbl.append(k[0])
        elif 'ENGLISH' in k[1]:
            english.append(k[0])
        else:
            grade_class.append(k[0])
        
            
    num = 0       
    
# 교양 패패과목 알려줘
# 00학부 전공과목 알려줘



    if len(professor) > 0:
        pre_info = pre_info[pre_info['교강사'] == professor[0]]

    if len(department) > 0:
        pre_info = pre_info[pre_info['설강학과'] == department[0]]
        # print(department[0])

    if len(evaluation) > 0:
        if evaluation[0] == '절대평가' or evaluation[0] == '절평':
            pre_info = pre_info[pre_info['평가'] == '절대평가']
        elif evaluation[0] == '상대평가' or evaluation[0] == '상평':
            pre_info = pre_info[pre_info['평가'] == '상대평가']
        else:
            pre_info = pre_info[pre_info['평가'] == 'P/F']

    if len(classification) > 0:
        if classification[0] == '필수':
            pre_info = pre_info[pre_info['이수구분'].str.contains('필수')]
        elif classification[0] == '교양':
            pre_info = pre_info[pre_info['이수구분'].str.contains('교양')]
        elif classification[0] == '전공':
            pre_info = pre_info[pre_info['이수구분'].str.contains('전공')]
        else:
            pre_info = pre_info[pre_info['이수구분'].str.contains(classification[0])]

    if len(field) > 0:
        pre_info = pre_info[pre_info['영역'].str.contains(field[0])]

    if len(pbl) > 0:
        pre_info = pre_info[pre_info['IC-PBL'] == 'Y']

    if len(english) > 0:
        pre_info = pre_info[pre_info['영어전용E'] == 'Y']

    
    if len(grade_class) > 0:
        for number in grade_class:
            # 학년 
            if number == '1학년' or number == '일학년':
                pre_info = pre_info[pre_info['학년'] == '1']

            elif number == '2학년' or number == '이학년':
                pre_info = pre_info[pre_info['학년'] == '2']

            elif number == '3학년' or number == '삼학년':
                pre_info = pre_info[pre_info['학년'] == '3']

            elif number == '4학년' or number == '사학년':
                pre_info = pre_info[pre_info['학년'] == '4']

            elif number == '1반' or number == '일반':
                pre_info = pre_info[pre_info['반'] == '1']
            
            elif number == '2반' or number == '이반':
                pre_info = pre_info[pre_info['반'] == '2']

            elif number == '3반' or number == '삼반':
                pre_info = pre_info[pre_info['반'] == '3']

            elif number == '4반' or number == '사반':
                pre_info = pre_info[pre_info['반'] == '4']

    name = list(pre_info['교과목명'])
    name = list(set(name))
    
    # print(name)
    result = ''
    for i in range(len(name)):
        if i == (len(name)-1):
            result += name[i]
        else:
            result += name[i] + ', '



    return "\"" + result + "\" (가)이 있습니다."

        








        
      