from django.db import models
from User.models import User
from Counselor.models import Counselor

class Review(models.Model):
    
    
    # 리뷰 정보 모델링 
    Max_Length = 100
    
    # 리뷰 PK
    review_id = models.AutoField(primary_key = True)
    # 내담자  PK
    user_pk = models.IntegerField()
    counselor_pk = models.IntegerField()
    
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # counselor_id = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    
    # 내담자 이름
    star = models.IntegerField()
    
    # 리뷰 내용
    review_contents = models.TextField()
    
    