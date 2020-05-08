from konlpy.tag import Mecab
from MeCab import Tagger

m = Mecab('/Users/jungyoon/Desktop/nlp/mecab-ko-dic-2.1.1-20180720')

inform_list = ['이메일','메일', '전화', '연락처', '연구실', '정보']

def get_prof_info_entity(sentence):
    words = m.pos(sentence)

    tagger = Tagger('-d %s' % '/Users/jungyoon/Desktop/nlp/mecab-ko-dic-2.1.1-20180720')

    entity = []
    keyword = []
    tag = []

    for word in words:
        temp = tagger.parse(word[0])
        parse = temp.split('\t')[0]
        if parse in inform_list:
            keyword.append(parse)
            tag.append('INFORM')
        category = temp.split('\t')[-1].split(',')[1]
        if category == '교수명':
            keyword.append(parse)
            tag.append('PROFESSOR')
    entity.append(keyword)
    entity.append(tag)
    
    return entity