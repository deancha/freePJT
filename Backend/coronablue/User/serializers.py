
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                  "user_pk",
                  "user_email" , 
                  "user_name" , 
                  "user_gender",
                  "user_password",
                  "user_age",
                  "issocial",
                  "isuser"
                  )