from django.db import models

class Counselor(models.Model):
    
    
    Max_Length = 100
    
    class meta: 
        pass
    
    # 내부적 id
    counselor_pk = models.AutoField(primary_key =True)
    
    # 상담사 pw
    counselor_pw = models.CharField(max_length=Max_Length)
    
    # 상담가 이름
    counselor_name = models.CharField(max_length=Max_Length)
    
    # 상담사 나이
    counselor_age  = models.IntegerField()
    
    # 상담사 성별
    counselor_gender = models.CharField(max_length=Max_Length)
    
    # 상담사 이메일 ( 아이디 )
    counselor_email = models.CharField(max_length=Max_Length)
   
    # 상담사 소개 
    counselor_introduce = models.CharField(max_length =Max_Length)

    # 프로필 이미지
    counselor_profile = models.CharField(max_length = 500, default="https://firebasestorage.googleapis.com/v0/b/glean-1a93c.appspot.com/o/counselor%2Fblank-profile-picture-973460_640.png?alt=media&token=d2aad89b-559a-4f39-b6eb-fcf39cfae6ff")

     # 고유 키
    key = models.BinaryField()
    
    # 상담사인지 사용자인지?
    isuser = models.IntegerField(default=1)
    
class Counselormajor(models.Model):
    
    # 내부적 id
    counselor_pk = models.AutoField(primary_key =True)
    
    # 청소년
    youth = models.BooleanField(default=False)
    
    # 노인
    senior = models.BooleanField(default=False)
    
    # 임산부
    pregnant = models.BooleanField(default=False)
    
    # 갱년기 
    menopause = models.BooleanField(default=False)
    
    # 약물 
    drug = models.BooleanField(default=False)
    
    # 암환자
    cancer = models.BooleanField(default=False)
    
    # 갑상선
    thyroid = models.BooleanField(default=False)
    
    # 계절성
    season = models.BooleanField(default=False)
    
    # etc
    etc = models.CharField(max_length=100, null=True)