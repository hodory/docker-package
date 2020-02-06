from konlpy.tag import Mecab, Kkma, Okt
from konlpy.utils import pprint
mecab = Mecab()
kkma = Kkma()
twitter = Okt()
string = '동해물과백두산이마르고닳도록'
print('# Mecab 형태소 분석')
pprint(mecab.morphs(string))
print('# 꼬꼬마 형태소 분석')
pprint(kkma.morphs(string))
print('# 트위터 형태소 분석')
pprint(twitter.morphs(string))
print('# 트위터 문구 추출')
pprint(twitter.phrases(string))