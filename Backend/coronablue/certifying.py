from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("headless")

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:/Users/multicampus/Desktop/SSAFY/PJT3/s03p31a104/Backend/coronablue/chromedriver.exe', options=options)

# C:/Users/multicampus/Desktop/SSAFY/PJT3/s03p31a104/Backend/coronablue/chromedriver.exe

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
# driver.implicitly_wait(3)

# url에 접근한다.
# driver.get('https://google.com')
driver.get('https://www.q-net.or.kr/qlf006.do?id=qlf00601&gSite=Q&gId=')


title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.content')))

lcs_kind = '0'
hangul_name = 'aaaaa'
dob = '930415'
lcs_num = '12345678901A'
issue_dob = '20070214'
lcs_mng_num = '0901234567'
lcs_mng_num1 = '12341234'
lcs_mng_num2 = '5678'

select = Select(driver.find_element_by_name('selLcs'))

if lcs_kind == '0':
    # driver.find_element_by_name('selLcs').send_keys(lcs_kind)
    select.select_by_value(lcs_kind)
    driver.find_element_by_id('hgulNm').send_keys(hangul_name)
    driver.find_element_by_id('resdNo1').send_keys(dob)
    driver.find_element_by_id('lcsNo').send_keys(lcs_num)
    driver.find_element_by_id('qualExpDt').send_keys(issue_dob)
    driver.find_element_by_id('lcsMngNo').send_keys(lcs_mng_num)

elif lcs_kind == '1':
    # driver.find_element_by_name('selLcs').send_keys(lcs_kind)
    select.select_by_value(lcs_kind)
    driver.find_element_by_id('hgulNm2').send_keys(hangul_name)
    driver.find_element_by_id('hrdNo1').send_keys(lcs_mng_num1)
    driver.find_element_by_id('hrdNo2').send_keys(lcs_mng_num2)

driver.find_element_by_xpath('//*[@id="content"]/div[2]/form[1]/div[2]/div[4]/button[2]').click()


# result = driver.find_element_by_xpath('//*[@id="PInfo"]/div/table/tbody/tr[1]/td/strong')
# result = driver.find_element_by_css_selector('#PInfo > div > table > tbody > tr:nth-child(1) > td > strong')
result = driver.find_element_by_class_name('fc_r')
print('result: ', result.text.encode('utf-8'))

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# result = soup.select('#PInfo > div > table > tbody > tr:nth-child(1) > td')   

# print('result: ', result)
# for r in result:
#     print(r.text.strip())

driver.quit()

