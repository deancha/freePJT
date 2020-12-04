from django.db import models

class User(models.Model):
    
    
    class Meta:
        pass
    
    # 사용자의 정보 모델링 
    Max_Length = 100
    # 내부 사용자 id
    user_pk = models.AutoField(primary_key=True)
    
    # 내담자 이메일 
    user_email = models.CharField(max_length=Max_Length, null=False)
    
    # 내담자 이름
    user_name = models.CharField(max_length=Max_Length)
    
    # 내담자 성별
    user_gender = models.CharField(max_length=Max_Length)
    
    # 내담자 비밀번호
    user_password = models.CharField(null=False , max_length=Max_Length)
    
    # 내담자 나이 
    user_age = models.IntegerField()
    
    # 소셜로그인 연동여부
    issocial = models.IntegerField(default=0)
        
    # 상담사인지 사용자인지?
    isuser = models.IntegerField(default=0)
   