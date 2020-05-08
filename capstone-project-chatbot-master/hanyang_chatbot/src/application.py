from entity.course_info.entity_recognizer import get_course_info_entity
from entity.prof_info.entity_recognizer import get_prof_info_entity
#from intent.classifier import get_intent
from scenario.course_professor_info import course_professor_info
from scenario.professor_inform import professor_inform



def run():
    while True:
        print('안녕하세요 여러분의 수강신청을 도와드리는 수강하냥! 입니다')
        print('과목정보를 찾으려면 1\n교수정보를 찾으려면 2\n수강정보를 찾으려면 3\n종료하려면 4를 입력하세요!')
        while True:
            intent = int(input())
            if intent in [1,2,3]:
                break
            elif intent == 4:
                print('수강하냥을 종료합니다 다음에 또 만나요!')
                quit()
            else:
                print('다시 입력하세요')
        print('Question : ', sep = '', end='')
        sentence = input()
            #   print('Preprocessed : ', sentence, sep='')
            #intent = '강의교수님'
        print('Intent : ', intent, sep='')
            # print(sentence)
        entity = get_entity(intent, sentence)
        print('Entity : ' + str(entity), sep='')

        answer = scenario(intent, entity)
        print('Answer : ' + answer, sep='', end='\n\n')

# def preprocess(sentence) -> str:

#     return sentence

def get_entity(intent, sentence):
    if intent == 1:
        return get_course_info_entity(sentence)
    elif intent == 2:
        return get_prof_info_entity(sentence)
    else:
        return None

def scenario(intent, entity) -> str:
    if intent == 1:
        return course_professor_info(entity)
    elif intent == 2:
        return professor_inform(entity)
    else:
        return '죄송합니다. 아직 그 정보는 잘 모르겠어요ㅠ ㅈㅅㅈㅅ'
