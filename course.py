from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

page = open('./course.html')
soup = BeautifulSoup(page, 'lxml')

subject = ['학년', '반', '이수구분', '영역', '수업번호', '학수번호',
           '(변경전)교과목명', '교과목명', '과목안내', '공학인증구분',
           '교강사','학점', '강의', '실습', '강좌유형',
           '수강정원', '수업시간', '강의실', '이수제한여부', '과목상세정보',
            '설강학과', '권장학과', '강의계획서']
# 0 학년
# 1 반
# 2 이수구분
# 3 영역
# 4 수업번호
# 5 학수번호
# 6 (변경전)교과목명
# 7 교과목명
# 8 과목안내
# 9 공학인증구분
# 10 교강사
# 11 학점
# 12 강의
# 13 실습
# 14 강좌유형
# 15 수강정원
# 16 수업시간
# 17 강의실
# 18 이수제한여부
# 19 과목상세정보
# 20 설강학과
# 21 권장학과
# 22 과목정보

even = soup.find_all(attrs={'class':'even'})
evens = []
for line in even:
    evens.append(line.text.split('\n'))

odd = soup.find_all(attrs={'class':'odd'})
odds = []
for line in odd:
    odds.append(line.text.split('\n'))

evens.extend(odds)

for i in range(len(evens)):
    evens[i] = evens[i][5:-1]
    b = evens[i][17].split('/')
    evens[i][17] = b[1]
    del evens[i][9]
    del evens[i][10]
    a = 'https://portal.hanyang.ac.kr/openPop.do?header=hidden&url=/haksa/SughAct/findSuupPlanDocHyIn.do&flag=DN&year=2020&term=10&suup='+str(evens[i][4])
    evens[i].append(a)

timetable = pd.DataFrame(evens, columns=subject)
timetable.to_csv('./'+'course.csv')