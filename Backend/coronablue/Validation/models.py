from django.db import models

# Create your models here.

class EmailValidation(models.Model):
    class Meta:
        pass

    email_pk = models.AutoField(primary_key=True)
    
    # user_name = models.CharField(max_length=50)

    request_email = models.CharField(max_length=50, null=False)

class NoteCertificateValidation(models.Model):
    class Meta:
        pass
    lcs_kind = models.CharField(max_length=10, default='0')
    hangul_name = models.CharField(max_length=50, null=False)
    dob = models.CharField(max_length=6)
    lcs_num = models.CharField(max_length=12)
    issue_dob = models.CharField(max_length=8)
    lcs_mng_num = models.CharField(max_length=10)

class CertCertificateValidation(models.Model):
    class Meta:
        pass
    lcs_kind = models.CharField(max_length=10, default='1')
    hangul_name = models.CharField(max_length=50, null=False)
    lcs_mng_num1 = models.CharField(max_length=8)
    lcs_mng_num2 = models.CharField(max_length=4)