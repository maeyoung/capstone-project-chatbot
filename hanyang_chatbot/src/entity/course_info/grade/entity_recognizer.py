# get_grade_entity(sentence) 학년 
from konlpy.tag import Mecab
from MeCab import Tagger

m = Mecab('/Users/maeyoung/mecab-ko-dic-2.1.1-20180720')

def get_grade_entity(sentence):
    words = m.pos(sentence)
    
    #print(words)
    
    tagger = Tagger('-d %s' % '/Users/maeyoung/mecab-ko-dic-2.1.1-20180720')
    
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
            keyword.append(parse)
            tag.append('SUBJECT')
        elif category == '교수명':
            keyword.append(parse)
            tag.append("PROFESSOR")
        elif category == '설강학과':
            keyword.append(parse)
            tag.append("DEPARTMENT")

            
    entity.append(keyword)
    entity.append(tag)
    
#     print(keyword, tag)
    return entity# entity 리턴


# 00과목 몇학년 수업이야?
# 00과목 