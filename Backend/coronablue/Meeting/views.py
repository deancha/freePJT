from django.shortcuts import render


# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializers import MeetingSerializer
from .serializers import MeetingvisitorSerializer
from .models import Meeting
from .models import Meetingvisitor

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

#time module
import datetime


# 1. 미팅 생성  
# 2. 생성된 미팅 참가
# 3. 시간으로 해당 사람들 조회
# 4. 상담자가 확인 후 승낙
# 5. 미팅 참여 여부 확인 

# 모임 만들기 insert
@api_view(['POST'])
@csrf_exempt
def meetinginsert(request):
    if request.method == "POST":
        serializer = MeetingSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data,"result":"success"}, status=200  , safe=False )
        return JsonResponse({"data":serializer.errors,"result":"fail"}, status=500  , safe=False )
    
# 모임 참가자 insert
@api_view(['POST'])
@csrf_exempt
def meetingvisitorinsert(request):
    if request.method == "POST":
        data= JSONParser().parse(request)
        meeting_pk = data['meeting_pk']
        obj = Meeting.objects.filter(meeting_pk =meeting_pk)
        num =dict(list(obj.values())[0])['meeting_now']
        obj.update(meeting_now=num+1) 
        
        serializer = MeetingvisitorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"},status=200  , safe=False )
        return JsonResponse({"data": serializer.errors,"result":"fail"}, status=500  , safe=False )

   
# 상담사 번호로 자신에게 할당된 모임을 조회 -> 매칭 대기상태만
@api_view(["GET"])
@csrf_exempt
def getmeetinglist(request , number):
    if request.method == "GET":
        return JsonResponse({"data": MeetingSerializer(Meeting.objects.filter(meeting_counselor =number , meetingmatching=False , done=False), many=True).data
                             ,"result":"success"}
                            , safe=False ,status=200)
       
# 상담사가 목록중 자신에게 할당된 상담중 매칭 대기 변경
# 변경된 상담예약은 시간알림의 대상이 됨
@api_view(['PUT'])
@csrf_exempt
def confirmmeeting(request,number):
    if request.method == "PUT":
        # 상담 예약 번호 -> 상태 변경
        obj = Meeting.objects.filter(meeting_pk =number)
        try:
            obj.update(meetingmatching=True)
            return JsonResponse({"data":dict(obj.values()[0]) , "result":"success"},safe=False,status=200)
        except:
            return JsonResponse({"result":"fail"},status=500 ,safe=False )

# 모임 완료 기능 
@api_view(['PUT'])
@csrf_exempt
def donemeeting(request , number):
    if request.method == "PUT":
        # 상담 예약 번호 -> 상태 변경
        # 상담에 참여한 사람들 것도 변경
        obj = Meeting.objects.filter(meeting_pk =number)
        user_objs= Meetingvisitor.objects.filter(meeting_pk =number)
        try:
            obj.update(done=True)
            user_objs.update(done=True)
            return JsonResponse({"data":dict(obj.values()[0]) , "result":"success"},safe=False,status=200)
        except:
            return JsonResponse({"result":"fail"},status=500,safe=False)
        
       
# 사용자번호로 예약조회 
@api_view(["GET"])
@csrf_exempt
def getmeetingReservation(request , number):
    if request.method == 'GET':
        return JsonResponse({"data":MeetingvisitorSerializer(Meetingvisitor.objects.filter(meetingvisitor_userpk =number , done =False), many=True).data
                             ,"result":"success"} , safe=False , status=200)
   
# 시간으로 알람 날릴 사용자들 조회
@api_view(["GET"])
@csrf_exempt
def alarmlist(request):
    if request.method == 'GET':
        res =dict()
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
        queryset = Meeting.objects.filter(meeting_startdate__date__lte=nowtime , meeting_enddate__date__gte=nowtime , done =False , meetingmatching=True)
        target = list()
        for item in list(queryset.values()):
            target.append(int(dict(item)['meeting_pk']))
        # target을 돌면서 알람 대상자들 추출
        res = list()
        for i in target:
            obj = Meetingvisitor.objects.filter(meeting_pk =i , done =False)
            if len (list(obj.values())) > 0 :
                for j in list(obj.values()):
                    res.append(j)
        if len(list(queryset.values())) >0 :
            return JsonResponse({"data":res , "result":"success"},status= 200, safe=False)
        return JsonResponse({"result":"현재시간에 모임대상자 없음"} , safe=False , status=200)


# 참석 가능한 미팅 리스트 로딩
@api_view(['GET'])
@csrf_exempt
def availablemeetinglist(request):
    if request.method == "GET":
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
        return JsonResponse({"data":MeetingSerializer(Meeting.objects.filter(meeting_startdate__date__lte=nowtime , meeting_enddate__date__gte=nowtime ,meetingmatching=True,recruiting=True,done=False), many=True).data , "result":"success"},status=200 , safe=False)

  