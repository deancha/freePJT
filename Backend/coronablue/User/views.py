from django.shortcuts import render, redirect


# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializers import UserSerializer
from .models import User
from Counselor.models import Counselor

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
            
            
# 사용자 입력 or 전체 조회 
@api_view(['POST','GET'])
@csrf_exempt
def userlist(request):
    if request.method == "POST":
        serializer = UserSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data,"result":"success"}, status=200, safe=False)
        return JsonResponse({"data":serializer.errors,"result":"fail"}, status=500, safe=False)
    elif request.method == "GET":
        userlist = UserSerializer(User.objects.all(), many=True)
        try:
            return JsonResponse({"data":userlist.data,"result":"success"}, status=200, safe=False)
        except:
            return JsonResponse({"data":"empty","result":"fail"}, status=500 ,safe=False)
    
@api_view(['POST'])
@csrf_exempt
def userlogin(request):
    if request.method == "POST":
        data=JSONParser().parse(request)
        userid = data['user_email']
        userpw = data['user_password']
        login = None
        try :
            login =User.objects.filter(user_email= userid , user_password = userpw).values()[0]
        except:
            try:
                login =Counselor.objects.filter(counselor_email =userid,counselor_pw=userpw).values()[0]
                del login['key']
            except:
                return JsonResponse({"data":"회원정보없음!","result":"fail"}, status=200, safe=False)
        return JsonResponse({"data":login,"result":"success"}, status=200, safe=False)
        
            
    

# 사용자번호로 조회 수정 삭제
@api_view(['GET',"DELETE","PUT"])
@csrf_exempt
def user(request , number):
    obj = User.objects.filter(user_pk =number)
    if request.method == 'GET':
        try:
            return JsonResponse({"data":UserSerializer(obj, many=True).data,"result":"success"}, status=200  , safe=False )
        except:
            return JsonResponse({"data":"empty","result":"fail"}, status=500 , safe=False )
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"data" : "delete okay","result":"success"}, status=200 , safe=False)
    elif request.method == "PUT":
        obj = User.objects.filter(user_pk =number).first()
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"},status=200,safe=False)
        return JsonResponse({"data":"empty","result":"fail"},status=500,safe=False)
    
    
# 이메일 중복체크 
@api_view(['POST'])
@csrf_exempt
def useremailcheck(request):
    if request.method == "POST":
        data=JSONParser().parse(request)
        email = data['user_email']
        res = User.objects.filter(user_email=email)
        if len(list(res)) > 0 :
            return JsonResponse({"data": "가입불가","result":"fail"} , status=200)
        return JsonResponse({"data": "가입가능","result":"success"} ,status=200)
    