from django.shortcuts import render


# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializers import CounselorSerializer
from .serializers import CounselormajorSerializer
from .models import Counselor
from .models import Counselormajor
# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

# 암호화
from cryptography.fernet import Fernet
import json

# 상담사 입력 or 전체 조회 

@api_view(['POST','GET'])
@csrf_exempt
def counselorlist(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        try:
            Counselor.objects.create(
                counselor_name = data['counselor_name'],
                 counselor_pw = data['counselor_pw'] ,  
                counselor_age = data['counselor_age'],
                counselor_gender = data['counselor_gender'],
                counselor_email = data['counselor_email'],
                counselor_introduce=data['counselor_introduce'],
                key = Fernet.generate_key(),
                counselor_profile =data['counselor_profile'],
                isuser=1
            )
            return JsonResponse({"result":"success" , "data" : data}, status=200  , safe=False)
        except:
            return JsonResponse({"result":"fail check data"}, status=500  , safe=False)
    elif request.method == "GET":
        userlist = CounselorSerializer(Counselor.objects.all(), many=True)
        return JsonResponse( {"data":userlist.data,"result":"success"}, safe=False , status=200  )
    

# 상담사번호로 조회 수정 삭제
@api_view(['GET',"DELETE","PUT"])
@csrf_exempt
def counselor(request , number):
    obj = Counselor.objects.filter(counselor_pk =number)
    if request.method == 'GET':
        return JsonResponse({"data":CounselorSerializer(obj, many=True).data , "result":"success"}  , safe=False, status=200)
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"result" : "sucess"}, safe=False, status=200)
    elif request.method == "PUT":
        obj = Counselor.objects.filter(counselor_pk =number).first()
        data = JSONParser().parse(request)
        serializer = CounselorSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"}, status=200 , safe=False)
        return JsonResponse({"data":"empty","result":"fail"},status=500 , safe=False)



# 상담사 필드 선정
@api_view(['POST','GET'])
@csrf_exempt
def counselormajorlist(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CounselormajorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data,"result":"success"}, status=200 , safe=False )
        else:
            return JsonResponse({"result":"fail"}, status=500 , safe=False)
    elif request.method == "GET":
        userlist = CounselormajorSerializer(Counselormajor.objects.all(), many=True)
        return JsonResponse({"data":userlist.data ,"result":"success"}, safe=False , status=200)
    
# 상담사번호로 조회 수정 삭제
@api_view(['GET',"DELETE","PUT"])
@csrf_exempt
def counselormajor(request , number):
    obj = Counselormajor.objects.filter(counselor_pk =number)
    if request.method == 'GET':
        return JsonResponse({"data":CounselormajorSerializer(obj, many=True).data  ,"result":"success" } , safe=False, status=200)
    elif request.method == "DELETE":
        obj.delete()
        return JsonResponse({"result" : "success"}, safe=False, status=200)
    elif request.method == "PUT":
        obj = Counselormajor.objects.filter(counselor_pk =number).first()
        data = JSONParser().parse(request)
        serializer = CounselormajorSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"},safe=False, status=200)
        return JsonResponse({"data":"empty","result":"fail"},status=500 ,safe=False)


    
    