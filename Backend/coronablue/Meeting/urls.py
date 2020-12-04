from django.contrib import admin
from django.urls import path, include

from Meeting import views



# 중간 라우터 연결에서 연결 
urlpatterns = [
   path("meetinginsert", views.meetinginsert),
   path("meetingvisitorinsert", views.meetingvisitorinsert),
   path("getmeetinglist/<int:number>", views.getmeetinglist),
   path("confirmmeeting/<int:number>", views.confirmmeeting),
   path("alarmlist", views.alarmlist),
   path("availablemeetinglist", views.availablemeetinglist),
   path("donemeeting/<int:number>", views.donemeeting),
   path("getmeetingReservation/<int:number>", views.getmeetingReservation),
]