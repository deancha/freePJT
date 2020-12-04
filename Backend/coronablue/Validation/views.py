from django.shortcuts import render, redirect

# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializers import EmailValidationSerializer, NoteCertificateValidationSerializer, CertCertificateValidationSerializer
from .models import EmailValidation, NoteCertificateValidation, CertCertificateValidation

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

# SEND EMAIL
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from random import randint

# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup


# Create your views here.
@api_view(['POST'])
@csrf_exempt
def emailvalidation(request):
    if request.method == "POST":
        serializer = EmailValidationSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            random_number = randint(10**5, 10**6)
            request_email = serializer.validated_data['request_email']
            mail_subject = "[G.Lean] 회원가입 인증 메일"
            message = "안녕하세요\n" "G.Lean 인증번호는 "+str(random_number)+" 입니다\n" "인증확인란에 넣어주세요"
            email = EmailMessage(mail_subject, message, to=[request_email])
            email.send()
           
            serializer.save()
            return JsonResponse({'random_number': random_number }, status=200)
        return JsonResponse(serializer.errors, status=404)

@api_view(['POST'])
@csrf_exempt
def notecertify(request):
    if request.method == "POST":
        serializer = NoteCertificateValidationSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            driver = webdriver.Chrome('C:/Users/multicampus/Desktop/SSAFY/PJT3/s03p31a104/Backend/coronablue/chromedriver.exe', options=options)
            
            driver.get('https://www.q-net.or.kr/qlf006.do?id=qlf00601&gSite=Q&gId=')
            title = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div.content')))

            lcs_kind = serializer.validated_data["lcs_kind"]
            hangul_name = serializer.validated_data["hangul_name"]
            dob = serializer.validated_data["dob"]
            lcs_num = serializer.validated_data["lcs_num"]
            issue_dob = serializer.validated_data["issue_dob"]
            lcs_mng_num = serializer.validated_data["lcs_mng_num"]

            select = Select(driver.find_element_by_name('selLcs'))

            select.select_by_value(lcs_kind)
            driver.find_element_by_id('hgulNm').send_keys(hangul_name)
            driver.find_element_by_id('resdNo1').send_keys(dob)
            driver.find_element_by_id('lcsNo').send_keys(lcs_num)
            driver.find_element_by_id('qualExpDt').send_keys(issue_dob)
            driver.find_element_by_id('lcsMngNo').send_keys(lcs_mng_num)

            driver.find_element_by_xpath('//*[@id="content"]/div[2]/form[1]/div[2]/div[4]/button[2]').click()
            result = driver.find_element_by_class_name('fc_r')

            is_real = True
            if result.text.encode('utf-8') == b'\xe2\x80\xbb \xec\xb5\x9c\xea\xb7\xbc \xeb\xb0\x9c\xea\xb8\x89\xec\x97\xb0\xec\x9b\x94\xec\x9d\xbc (\xeb\x98\x90\xeb\x8a\x94 \xeb\x93\xb1\xeb\xa1\x9d\xeb\x85\x84\xec\x9b\x94\xec\x9d\xbc) \xea\xb8\xb0\xec\x9e\xac':
                is_real = False
            
            return JsonResponse({'is_real': is_real}, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
@csrf_exempt
def certcertify(request):
    if request.method == "POST":
        serializer = CertCertificateValidationSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            pass