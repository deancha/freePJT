from konlpy.tag import Okt  

from lexrankr import LexRank


def getAdjectice(text):
    okt = Okt()
    sentences_tag = okt.pos(text , stem=True)
    noun_adj_list = []
    for sentence in sentences_tag:
        print(sentence)
        if sentence[1] == 'Adjective' :
            noun_adj_list.append(sentence)
    return noun_adj_list

def getsummery(text):
    lexrank = LexRank()
    lexrank.summarize(text)
    return lexrank.probe(None)
text = """
상담시작일시 : 20년 11월 10일 , 10시 ,상담종료일시 : 20년 11월 10일 , 12시
상담 3회차이다. 내담자는 지난 트라우마로 인하여 고생하였지만, 반복되는 상담으로 자존감을많이 회복한 듯하다. 지속적인 약물 치료는 필요해 보인다. 
"""

print(getAdjectice(text))
print(getsummery(text))