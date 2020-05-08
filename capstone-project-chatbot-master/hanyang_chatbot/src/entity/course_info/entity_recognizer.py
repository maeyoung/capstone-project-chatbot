# get course information entity
from konlpy.tag import Mecab
from MeCab import Tagger

m = Mecab('/Users/jungyoon/Desktop/nlp/mecab-ko-dic-2.1.1-20180720')
# ret = m.pos("IC-PBL과취창업을위한진로탐색이랑 응용유기공업화학 교수님 알려줘")
# ret

def get_course_info_entity(sentence):
    words = m.pos(sentence)

    # print(words)
    tagger = Tagger('-d %s' % '/Users/jungyoon/Desktop/nlp/mecab-ko-dic-2.1.1-20180720')

    entity = []
    keyword = []
    tag = []

    for word in words:
        # print(word)
        temp = tagger.parse(word[0])
        #print('temp\t' + temp)
        parse = temp.split('\t')[0] # 잘려진 단어
        # print(parse)
        category = temp.split('\t')[-1].split(',')[1]
        # print('의미\t' + category)
        if category == '과목명':
            # print('찾고자하는 과목은 \'' + parse + '\' 입니다.')
            keyword.append(parse)
            tag.append('SUBJECT')
#         elif category == '교수명':
#             # print('교수이름 : ' + parse)
#             keyword.append(parse)
#             tag.append('PROFESSOR')

    entity.append(keyword)
    entity.append(tag)

#     print(keyword, tag)
    return entity# entity 리턴