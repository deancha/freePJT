from django.contrib import admin
from django.urls import path, include

from Counselor import views

urlpatterns = [
    path("counselorlist", views.counselorlist),
    path("counselor/<int:number>", views.counselor),
    path("counselormajorlist", views.counselormajorlist),
    path("counselormajor/<int:number>", views.counselormajor),
]