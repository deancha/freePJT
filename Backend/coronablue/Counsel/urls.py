from django.contrib import admin
from django.urls import path, include

from Counsel import views

urlpatterns = [
    path("counselReservationinsert", views.counselReservationinsert),
    path("counselinsert", views.counselinsert),
    path("counselReservation/<int:number>", views.counselReservation),
    path("counsel/<int:number>", views.counsel),
    path("getcounselReservation/<int:number>", views.getcounselReservation),
    path("getcounsel/<int:number>", views.getcounsel),
    path("getmycounsel/<int:number>", views.getmycounsel),
    path("confirmcounselReservation/<int:number>", views.confirmcounselReservation),
    path("alarmlist", views.alarmlist),
    path("counseleddocument", views.counseleddocument),
        
]