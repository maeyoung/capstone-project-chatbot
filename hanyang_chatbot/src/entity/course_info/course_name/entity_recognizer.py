# get_before_name_entity(sentence)
from konlpy.tag import Mecab
from MeCab import Tagger

m = Mecab('/Users/maeyoung/mecab-ko-dic-2.1.1-20180720')

def get_name_entity(sentence): 
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
        if category == '교수명':
            keyword.append(parse)
            tag.append("PROFESSOR")
        elif category == '학과명':
            keyword.append(parse)
            tag.append("DEPARTMENT")
        elif category == '평가기준':
            keyword.append(parse)
            tag.append("EVALUATION")
        elif category == '학년':
            keyword.append(parse)
            tag.append("GRADE")
        elif category == '반':
            keyword.append(parse)
            tag.append("CLASSROOM")
        elif category == '이수구분':
            keyword.append(parse)
            tag.append("CLASSIFICATION")
        elif category == '영역':
            keyword.append(parse)
            tag.append("FIELD")
        elif category == '피비엘':
            keyword.append(parse)
            tag.append("PBL")
        elif category == '영어전용':
            keyword.append(parse)
            tag.append("ENGLISH")

            
    entity.append(keyword)
    entity.append(tag)
    
#     print(keyword, tag)
    return entity# entity 리턴