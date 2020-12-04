from django.db import models
from User.models import User
from Counselor.models import Counselor

class Counsel(models.Model):
    
   # 상담 pk
    counsel_pk = models.AutoField(primary_key=True)
    
    # 유저(내담자)
    user_pk = models.IntegerField()

     # 상담 시작일자
    counsel_startdate = models.DateTimeField()
    
    # 상담 끝일자
    counsel_enddate = models.DateTimeField()
    
    # 상담사
    counselor_pk = models.IntegerField()

    # 상담내용
    counsel_detail = models.BinaryField()
    
    # 완료 여부
    counselReservation_pk = models.IntegerField()
    
    # 상담 요금
    counsel_fee = models.IntegerField()
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
   

class CounselReservation(models.Model):
       
    # 상담 예약 pk
    counselReservation_pk = models.AutoField(primary_key=True)
    
    # 상담 시작일자
    counsel_startdate = models.DateTimeField()
    
    # 상담 끝일자
    counsel_enddate = models.DateTimeField()
    
    # 유저(내담자)
    user_pk = models.IntegerField()

    # 상담사
    counselor_pk = models.IntegerField()
    
    # 상담여부
    done = models.BooleanField(default=False)
    
    # 상담사 승인 여부
    matching = models.BooleanField(default=False)
    
    # 상담 요금
    counsel_fee = models.IntegerField()

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)