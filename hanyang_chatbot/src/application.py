# from entity.course_info.professor.entity_recognizer import get_course_professor_entity
# from entity.course_info.before_name.entity_recognizer import get_before_name_entity
# from entity.course_info.grade.entity_recognizer import get_grade_entity
# from entity.course_info.classroom.entity_recognizer import get_classroom_entity
# from entity.course_info.department.entity_recognizer import get_department_entity
from entity.course_info.entity_recognizer import get_normal_entity
from entity.course_info.evaluation.entity_recognizer import get_evaluation_entity
from entity.course_info.course_name.entity_recognizer import get_name_entity
#from intent.classifier import get_intent
from scenario.course_info.professor.professor import course_professor
from scenario.course_info.before_name.before_name import before_name
from scenario.course_info.grade.grade import grade
from scenario.course_info.classroom.classroom import classroom
from scenario.course_info.department.department import department
from scenario.course_info.isu_classification.isu_classification import isu_classification
from scenario.course_info.course_number.course_number import course_number
from scenario.course_info.course_grade.course_grade import course_grade
from scenario.course_info.course_time.course_time import course_time
from scenario.course_info.student_number.student_number import student_number
from scenario.course_info.timetable.timetable import timetable
from scenario.course_info.isu_limit.isu_limit import isu_limit
from scenario.course_info.syllabus.syllabus import syllabus
from scenario.course_info.evaluation.evaluation import evaluation
from scenario.course_info.course_name.course_name import course_name
from scenario.course_info.field.field import field


# 처음에 버튼으로 강의정보, 교수정보, 수강신청안내를 나눈다.
# 여기서는 강의정보안에서 분류된 intent별로 답변을 생성해줘야 함  

def run():
    while True:
        # 나중에 지울거임 
        print('Intent = [강의교수님, 과목명, 학년, 이수구분, 영역, 학수번호, 변경전교과목명, 학점, 강의시간(실습), 강좌유형(X), 수강정원, 수업시간, 강의실, 이수제한, 학과, 강의계획서, 평가방법]')
        print('Intent :', sep = '', end='')
        intent = input().replace(" ","")
        # print(intent)
        
        print('Question : ', sep = '', end='')
        sentence = input().replace(" ","")

        # intent = '과목명'  # 외부에서 학습으로 받아와야 됨 
        print('Intent : ', intent, sep='')
        # print(sentence)

        entity = get_entity(intent, sentence)
        print('Entity : ' + str(entity), sep='')

        answer = scenario(intent, entity)
        # print(type(answer))
        if not answer:
            print('Answer : 엔티티가 검출되지 않았습니다.')
        else: 
            print('Answer : ' + answer, sep='', end='\n\n')

# def preprocess(sentence) -> str:

#     return sentence

def get_entity(intent, sentence):
    if intent == '과목명':
        return get_name_entity(sentence)
    elif intent == '평가방법':
        return get_evaluation_entity(sentence)
    else:
        return get_normal_entity(sentence)


"""
def get_entity(intent, sentence):
    if intent == '강의교수님':
        return get_course_professor_entity(sentence)
    elif intent == '과목명':
        return get_course_name_entity(sentence)
    elif intent == '학년':
        return get_grade_entity(sentence)
    elif intent == '이수구분':
        return get_isu_classification_entity(sentence)
    elif intent == '학수번호':
        return get_course_number_entity(sentence)
    elif intent == '변경전교과목명':
        return get_before_name_entity(sentence)
    elif intent == '학점':
        return get_course_grade_entity(sentence)
    elif intent == '강의시간(실습)':
        return get_course_time_entity(sentence)
    elif intent == '강좌유형':
        return get_course_type_entity(sentence)
    elif intent == '수강정원':
        return get_student_number_entity(sentence)
    elif intent == '수업시간':
        return get_timetable_entity(sentence)
    elif intent == '강의실':
        return get_classroom_entity(sentence)
    elif intent == '이수제한':
        return get_isu_limit_entity(sentence)
    elif intent == '과목상세정보':
        return get_course_more_info_entity(sentence)
    elif intent == '학과':  #설강학과기준
        return get_department_entity(sentence)
    elif intent == '강의계획서':
        return get_syllabus_entity(sentence)
    else:
        return None
"""

def scenario(intent, entity) -> str:
    if intent == '강의교수님':
        return course_professor(entity)
    elif intent == '과목명':
        return course_name(entity)
    elif intent == '학년':
        return grade(entity)
    elif intent == '이수구분':
        return isu_classification(entity)
    elif intent == '영역':
        return field(entity)  ###### 작성해야됨 
    elif intent == '학수번호':
        return course_number(entity)
    elif intent == '변경전교과목명':
        return before_name(entity)
    elif intent == '학점':
        return course_grade(entity)
    elif intent == '강의시간(실습)':
        return course_time(entity)
    elif intent == '강좌유형':
        return course_type(entity)
    elif intent == '수강정원':
        return student_number(entity)
    elif intent == '수업시간':
        return timetable(entity)
    elif intent == '강의실':
        return classroom(entity)
    elif intent == '이수제한':
        return isu_limit(entity)
    elif intent == '과목상세정보':
        return course_more_info(entity)
    elif intent == '학과':
        return department(entity)
    elif intent == '강의계획서':
        return syllabus(entity)
    elif intent == '평가방법':
        return evaluation(entity)
    else:
        return '죄송합니다. 아직 그 정보는 잘 모르겠어요ㅠ ㅈㅅㅈㅅ'





# xx학과 2학년 전공과목 알려줘  -> 과목명
# 학수번호 비교
# 월요일 9시 수업 뭐잇어?