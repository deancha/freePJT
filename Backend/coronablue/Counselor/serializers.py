from rest_framework import serializers
from .models import Counselor
from .models import Counselormajor


class CounselorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Counselor
        fields = (
            "counselor_pk",
            "counselor_name",
            "counselor_age",
            "counselor_gender",
            "counselor_pw",
            "counselor_introduce",
            "counselor_email",
            "counselor_profile",
            "key",
            "isuser"
        )


class CounselormajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Counselormajor
        fields = ("counselor_pk",
                  "youth",
                  "senior",
                  "pregnant",
                  "menopause",
                  "drug",
                  "cancer",
                  "thyroid",
                  "season",
                  "etc",
                  )
