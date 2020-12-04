from django.shortcuts import render

# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializers import CounselSerializer
from .serializers import CounselReservationSerializer
from Counselor.serializers import CounselorSerializer
from .models import Counsel
from .models import CounselReservation
from .models import Counselor

from User.models import User
from Counsel.models import CounselReservation

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

# 상담일지 암호화
from cryptography.fernet import Fernet
import base64
import chardet


#time module
import datetime


# 1. 내담자 pk와 상담자 pk로 예약 insert
# 2. 내담자 pk로 예약 조회
# 3. 내담자 pk와 상담자 pk로 상담내용 insert
# 4. 상담 예약 pk로 수정 삭제 정보조회 등등

  
# 사용자번호로 예약조회 
@api_view(["GET"])
@csrf_exempt
def getcounselReservation(request , number):
    if request.method == 'GET':
        return JsonResponse({"data":CounselReservationSerializer(CounselReservation.objects.filter(user_pk=number , matching=True), many=True).data
            ,  "result":"success"},safe=False , status=200)
   
# 사용자번호로 조회 
@api_view(["GET"])
@csrf_exempt
def getcounsel(request , number):
    if request.method == 'GET':
        return JsonResponse({"data":CounselSerializer(Counsel.objects.filter(user_pk =number), many=True).data,
                             "result":"success"}  , safe=False , status=200)
   
# 상담예약 insert
@api_view(['POST'])
@csrf_exempt
def counselReservationinsert(request):
    if request.method == "POST":
        serializer = CounselReservationSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data,"result":"success"}, status=200 , safe=False)
        return JsonResponse({"data":serializer.errors,"result":"fail"}, status=500 , safe=False)
    
# 상담 insert
@api_view(['POST'])
@csrf_exempt
def counselinsert(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        # 암호화
        counselor = Counselor.objects.filter(counselor_pk = data['counselor_pk']).values()
        key = dict(counselor[0])['key']
        text = data['counsel_detail'].encode('utf-8')
        data.update({"counsel_detail": Fernet(key).encrypt(text)})  
        try:
            obj=CounselReservation.objects.filter(counselReservation_pk =data['counselReservation_pk'])
            obj.update(done=True)
            Counsel.objects.create(
                user_pk = data['user_pk'],
                counselor_pk = data['counselor_pk'],
                counsel_startdate = data['counsel_startdate'],
                counselReservation_pk=data['counselReservation_pk'],
                counsel_enddate = data['counsel_enddate'],
                counsel_detail=data['counsel_detail'],
                counsel_fee=data['counsel_fee']
            )
            return JsonResponse({"result":"success"}, status=200 , safe=False)
        except:
            return JsonResponse({"result":"fail"}, status=500 , safe=False)
    
# 상담예약 번호로 수정 삭제
@api_view(["DELETE","PUT"])
@csrf_exempt
def counselReservation(request , number):
    
    obj = CounselReservation.objects.filter(counselReservation_pk =number)
    if request.method == "DELETE":
        obj.delete()
        return JsonResponse({"result" : "success"}, safe=False , status=200)
    elif request.method == "PUT":
        obj = CounselReservation.objects.filter(counselReservation_pk =number).first()
        data = JSONParser().parse(request)
        serializer = CounselReservationSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"},safe=False,status=200)
        return JsonResponse({"result":"fail","data":"empty"},status=500 ,safe=False)

# 상담 번호로 수정 삭제
@api_view(["DELETE","PUT"])
@csrf_exempt
def counsel(request , number):
    
    obj = Counsel.objects.filter(counsel_pk =number)
    
    if request.method == "DELETE":
        obj.delete()
        return JsonResponse({"result" : "success"}, safe=False ,status=200 )
    elif request.method == "PUT":
        obj = Counsel.objects.filter(counsel_pk =number).first()
        data = JSONParser().parse(request)
        serializer = CounselSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"},safe=False,status=200)
        return JsonResponse({"result":"fail"},status=500,safe=False) 

@api_view(["GET"])
@csrf_exempt
def getmycounsel(request , number):
    if request.method == "GET":
        answer = dict()
        data = CounselReservationSerializer(CounselReservation.objects.filter(counselor_pk =number , matching=False), many=True).data
        res = list()
        for d in data :
            Username = User.objects.filter(user_pk=dict(d)['user_pk'])
            u = Username.values()
            for i in u :
                res.append([ dict(d), {"name":i['user_name'] }])
                
                
        answer['listone'] = res
        
        data = CounselReservationSerializer(CounselReservation.objects.filter(counselor_pk =number , matching=True, done =False), many=True).data
        res = list()
        for d in data :
            Username = User.objects.filter(user_pk=dict(d)['user_pk'])
            u = Username.values()
            for i in u :
                res.append([ dict(d), {"name":i['user_name'] }])
        answer['listtwo'] = res
        
        data = CounselReservationSerializer(CounselReservation.objects.filter(counselor_pk =number , matching=True, done =True), many=True).data
        res = list()
        for d in data :
            Username = User.objects.filter(user_pk=dict(d)['user_pk'])
            u = Username.values()
            for i in u :
                res.append([ dict(d), {"name":i['user_name'] }])
        answer['listthree'] = res
        
        return JsonResponse({"data": answer,"result":"success"}  , safe=False ,status=200)


   
# 상담사가 목록중 자신에게 할당된 상담중 매칭 대기 변경
# 변경된 상담예약은 시간알림의 대상이 됨
@api_view(['PUT'])
@csrf_exempt
def confirmcounselReservation(request , number):
    if request.method == "PUT":
        # 상담 예약 번호 -> 상태 변경
        obj = CounselReservation.objects.filter(counselReservation_pk =number)
        try:
            obj.update(matching=True)
            return JsonResponse({"data":dict(obj.values()[0]) , "result":"success"},safe=False,status=200)
        except:
            return JsonResponse({"data":"fail"},status=500 ,safe=False)

# 시간으로 알람 날릴 사용자들 조회
@api_view(["GET"])
@csrf_exempt
def alarmlist(request):
    if request.method == 'GET':
        res =dict()
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
        queryset = CounselReservation.objects.filter(meeting_startdate__date__lte=nowtime , meeting_enddate__date__gte=nowtime  , matching =True, done=False)
        
        if len(list(queryset.values()))  >0 :
            return JsonResponse({"data":list(queryset.values()) , "result":"success","message":"알람대상자"},status= 200, safe=False)
        return JsonResponse({"result":"현재시간에 모임대상자 없음"} , safe=False , status=200)
    


 # 상담사가 자신이 상담한 상담 세부 내역 조회
@api_view(["POST"])
@csrf_exempt
def counseleddocument(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        counselor_number = data['counselor_pk']
        counselReservation_number = data['counselReservation_pk']
        counsel_number = Counsel.objects.get(counselReservation_pk = counselReservation_number)
        counsel_number = int(counsel_number.counsel_pk)
        counselor = Counselor.objects.filter(counselor_pk = counselor_number).values()
        key = dict(counselor[0])['key']
        queryset = Counsel.objects.filter(counsel_pk=counsel_number)
        description =list(queryset.values())[0]['counsel_detail']
        decode_description = Fernet(key).decrypt(bytes(description)).decode("utf-8")
        updatedata = dict(list(queryset.values())[0])
        res = {
            "user_pk" : updatedata['user_pk'],
            "counsel_startdate" : updatedata['counsel_startdate'],
            "counsel_enddate" : updatedata['counsel_enddate'],
            "counselor_pk" : updatedata['counselor_pk'],
            "counsel_detail" : decode_description
        }
        try:
            return JsonResponse({"data":res , "result":"success"},status = 200, safe=False)
        except:
            return JsonResponse({"result":"fail"} , safe=False , status=500)
    