from django.db import models

class Meeting(models.Model):
    class meta:
        pass
    
    
    # 미팅번호
    meeting_pk = models.AutoField(primary_key=True)
    
    # 미팅 최대사람수 
    meeting_max = models.IntegerField()
    
    # 미팅 참여 사람 수
    meeting_now = models.IntegerField(default=1)
    
    # 미팅 시작
    meeting_startdate = models.DateTimeField()
    
    # 미팅 끝
    meeting_enddate = models.DateTimeField()
    
    # 미팅 제목
    meeting_title = models.CharField(max_length=100)
    
    # 미팅 주관자
    meeting_owner = models.IntegerField()
    
    # 미팅 담당 상담자
    meeting_counselor = models.IntegerField()
    
    # 미팅 담당자 수락 여부
    meetingmatching = models.BooleanField(default=False)
    
    # 미팅 끝남 여부 
    done = models.BooleanField(default=False)
    
    # 미팅 모집 중 여부
    recruiting = models.BooleanField(default=True)
class Meetingvisitor(models.Model):
    
    class meta:
        pass
    
    meetingvisitor_pk = models.AutoField(primary_key=True)
    
    meeting_pk = models.IntegerField()

    meetingvisitor_userpk = models.IntegerField()
    
    meetingvisitor_reportdate = models.DateTimeField()
    
    done = models.BooleanField(default=False)