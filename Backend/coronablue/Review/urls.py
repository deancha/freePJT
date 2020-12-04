from django.contrib import admin
from django.urls import path, include

from Review import views



# 중간 라우터 연결에서 연결 
urlpatterns = [
    path("reviewlist", views.reviewlist),
    path("review/<int:number>", views.review),
    path("getreviewuser/<int:number>", views.getreviewuser),
    path("getreviewcounselor/<int:number>", views.getreviewcounselor),
]