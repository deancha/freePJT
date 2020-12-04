# 계정
from django.contrib import admin

# swagger 연결 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# url 연결에 필요한 url method loading 
from django.urls import path
from django.urls import include


def get_swagger_schema_view():
    
    swagger_schema_url_patterns = [

        # 관리자 페이지 ID :SSAFY / PW : SSAFY
        path("admin/", admin.site.urls),
        
        # 내담자 회원가입 관련 페이지 
        path('user/',include("User.urls")),

        # 리뷰
        path('review/', include("Review.urls")),
        
        # 내담자 
        path('user/',include("User.urls")),

        # 상담사
        path('counselor/', include("Counselor.urls")),
        
        # 상담 예약 및 상담 
        path('counsel/', include("Counsel.urls")),
        
        # 모임 예약 및 상담 
        path('meeting/', include("Meeting.urls")),

        # 이메일 인증
        path('validation/', include("Validation.urls")),
    ]

    schema_view = get_schema_view(

        openapi.Info(
            title="Glean",
            default_version="v1",
            description='''
            
            Glean API 문서입니다
            
            ''',
            terms_of_service = 'https://google.com/policies/terms/',
            contact =openapi.Contact(email="gotkddnjs@naver.com"),
            license =openapi.License(name="sotaSangwon"),
        ),
        validators =['flex'],
        public = True,
        permission_classes=(AllowAny,),
        patterns = swagger_schema_url_patterns,
    )
    return schema_view