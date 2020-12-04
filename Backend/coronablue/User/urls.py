from django.contrib import admin
from django.urls import path, include

from User import views

app_name = 'user'

# 중간 라우터 연결에서 연결 
urlpatterns = [
    path("userlist", views.userlist),
    path("useremailcheck", views.useremailcheck),
    path("userlogin", views.userlogin),
    path("user/<int:number>", views.user),
]