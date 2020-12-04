
from rest_framework import serializers
from .models import Meeting
from .models import Meetingvisitor


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = (
                  "meeting_pk",
                  "meeting_max",
                  "meeting_now",
                  "meeting_startdate" , 
                  "meeting_enddate",
                  "meeting_title",
                  "meeting_owner",
                  "meeting_counselor",
                  "meetingmatching",
                  "done",
                  "recruiting"
                  )
        
        

class MeetingvisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetingvisitor
        fields = (
            "meeting_pk",
                    "meetingvisitor_pk" , 
                  "meetingvisitor_userpk" , 
                  "meetingvisitor_reportdate",
                "done"
                  )



