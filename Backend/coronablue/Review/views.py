from django.shortcuts import render

# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# INNER MODEL MODULE
from .serializer import ReviewSerializer
from .models import Review

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Avg, Max


# 리뷰 입력
@api_view(['POST'])
@csrf_exempt
def reviewlist(request):
    if request.method == "POST":
        serializer = ReviewSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data,"result":"success"}, status=200 , safe=False)
        return JsonResponse({"data":serializer.errors,"result":"fail"}, status=500 , safe=False)
 
# 사용자번호로 리뷰 전체 조회
@api_view(['GET'])
@csrf_exempt
def getreviewuser(request , number):
    if request.method == 'GET':
        return JsonResponse({"data":ReviewSerializer(Review.objects.filter(user_pk =number), many=True).data ,"result":"success"} , status=200, safe=False)
    
# 리뷰 번호로 삭제 및 수정 
@api_view(["DELETE","PUT"])
@csrf_exempt
def review(request , number):

    obj = Review.objects.filter(review_id =number)
    if request.method == "DELETE":
        obj.delete()
        return JsonResponse({"data" : "삭제완료","result":"success"}, status=200, safe=False)
    elif request.method == "PUT":
        obj = Review.objects.filter(review_id =number).first()
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data":serializer.data , "result":"success"}, status=200 ,safe=False)
        return JsonResponse({"data":"emtpy","result":"fail"},status=500 ,safe=False)
    

# 상담사 번호의 리뷰와 해당 상담사의 전체 평점 계산
@api_view(["GET"])
@csrf_exempt
def getreviewcounselor(request , number):
    if request.method == "GET":
        star = Review.objects.filter(counselor_pk=number).aggregate(Avg('star'))
        reviewlist = ReviewSerializer(Review.objects.filter(counselor_pk=number), many=True).data
        data = {"star" : star , "reviewlist" : reviewlist}
        return JsonResponse({"data": data ,"result":"success"}  , status=200 , safe=False)
   
     
    
    
    
    