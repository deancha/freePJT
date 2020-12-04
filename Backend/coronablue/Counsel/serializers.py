from rest_framework import serializers
from .models import Counsel
from .models import CounselReservation

class CounselSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Counsel
        fields = (
                  "counsel_pk" ,
                  "counsel_startdate",
                  "counsel_enddate",
                  "user_pk",
                  "counselor_pk",
                  "counsel_detail",
                  "counselReservation_pk",
                  "counsel_fee"
                  )
        
class CounselReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CounselReservation
        fields = (
                "counselReservation_pk",
                "counsel_startdate",
                "counsel_enddate",
                "user_pk",
                "counselor_pk",
                "done",
                "matching",
                "counsel_fee"
                )