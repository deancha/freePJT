# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('https://www.q-net.or.kr/qlf006.do?id=qlf00601&gSite=Q&gId=')
# HTML 소스 가져오기
html = req.text
# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')


# CSS Selector를 통해 html요소들을 찾아낸다.
info = {
    "hangul_name" : soup.select(
        '#hgulNm'
        ),
    "dob" : soup.select(
        '#resdNo1'
        ),
    "license_num" : soup.select(
        '#lcsNo'
        ),
    "issue_date" : soup.select(
        '#qualExpDt'
        ),
    "license_mng_num" : soup.select(
        '#lcsMngNo'
        ),
}

print(info)