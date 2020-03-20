from entity.course_info.entity_recognizer import get_course_info_entity
#from intent.classifier import get_intent
from scenario.course_professor_info import course_professor_info



def run():
    while True:
        print('Question : ', sep = '', end='')
        sentence = input()

        #   print('Preprocessed : ', sentence, sep='')

        intent = '강의교수님'
        print('Intent : ', intent, sep='')
        # print(sentence)
        entity = get_entity(intent, sentence)
        print('Entity : ' + str(entity), sep='')

        answer = scenario(intent, entity)
        print('Answer : ' + answer, sep='', end='\n\n')

# def preprocess(sentence) -> str:

#     return sentence

def get_entity(intent, sentence):
    if intent == '강의교수님':
        return get_course_info_entity(sentence)

    else:
        return None

def scenario(intent, entity) -> str:
    if intent == '강의교수님':
        return course_professor_info(entity)
    
    else:
        return '죄송합니다. 아직 그 정보는 잘 모르겠어요ㅠ ㅈㅅㅈㅅ'
