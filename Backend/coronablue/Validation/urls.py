from django.contrib import admin
from django.urls import path, include

from Validation import views



# 중간 라우터 연결에서 연결 
urlpatterns = [
    path("emailvalidation", views.emailvalidation, name="emailvalidation"),
    path("notecertify", views.notecertify, name="notecertify"),
    path("certcertify", views.certcertify, name="certcertify"),
]