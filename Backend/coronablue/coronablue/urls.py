from django.contrib import admin


# url 연결에 필요한 url method loading
from django.urls import path
from django.urls import include

# swagger loading
from .swagger import get_swagger_schema_view

# direct social login
from SocialLogin.views import kakao_login
from SocialLogin.views import kakao_callback
from SocialLogin.views import google_callback
from SocialLogin.views import kakao_login_check


schema_view = get_swagger_schema_view()

urlpatterns = [

    # SWAGGER같은 연결을 위한 URL
    path('swagger<str:format>', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui("swagger",
                                         cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

    # 관리자 페이지 이동
    path('admin/', admin.site.urls),

    # 내담자
    path('user/', include("User.urls")),

    # 상담사
    path('counselor/', include("Counselor.urls")),

    # 리뷰
    path('review/', include("Review.urls")),

    # 상담 예약 및 상담
    path('counsel/', include("Counsel.urls")),

    # 모임 예약 및 상담
    path('meeting/', include("Meeting.urls")),

    # 인증
    path('validation/', include("Validation.urls")),
    
    # 소셜 로그인
    path('account/login/kakao/', kakao_login),
    path('account/login/kakao/callback/', kakao_callback),
    path('account/login/kakao/callback/check/', kakao_login_check),

    path("accounts/", include("allauth.urls")),
    path("accounts/", include("rest_auth.urls")),
    path("accounts/profile/", google_callback),
]
