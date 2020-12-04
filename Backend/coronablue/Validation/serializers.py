from rest_framework import serializers
from .models import EmailValidation, NoteCertificateValidation, CertCertificateValidation


class EmailValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailValidation
        fields = ( 
                  "request_email" ,
                #   "user_name",
                  )

class NoteCertificateValidationSerializer(serializers.ModelSerializer):
  class Meta:
    model = NoteCertificateValidation
    fields = (
      "lcs_kind",
      "hangul_name",
      "dob",
      "lcs_num",
      "issue_dob",
      "lcs_mng_num",
    )

class CertCertificateValidationSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "lcs_kind",
      "hangul_name",
      "lcs_mng_num1",
      "lcs_mng_num2",
    )