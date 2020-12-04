import os

import my_settings

EMAIL_BACKEND = my_settings.EMAIL['EMAIL_BACKEND']
EMAIL_USE_TLS = my_settings.EMAIL['EMAIL_USE_TLS']
EMAIL_PORT = my_settings.EMAIL['EMAIL_PORT']
EMAIL_HOST = my_settings.EMAIL['EMAIL_HOST']
EMAIL_HOST_USER = my_settings.EMAIL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = my_settings.EMAIL['EMAIL_HOST_PASSWORD']
SERVER_EMAIL = my_settings.EMAIL['SERVER_EMAIL']
DEFAULT_FROM_MAIL = my_settings.EMAIL['DEFAULT_FROM_MAIL']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'f2)nuki$4i-dia^fdxdc)0k7o1b*49=k^7w9czn4%4(dmymz#3'

DEBUG = True

# Avoding Cors
ALLOWED_HOSTS = ["*"]

SWAGGER_SETTINGS = {
'JSON_EDITOR': True,
}
# for kakao login
SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id': os.environ.get('KAKAO_RSETAPI_KEY'),
            'secret': os.environ.get('KAKAO_APP_ID'),
            'key': ''
        }
    }
}

# 내가만든 app 등록 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",

    # cross origin
    'corsheaders',

    # allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    
    # provider 
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.naver",
    
    
    # 우리가 만든 App
    "User",
    "Counselor",
    "Review",
    "SocialLogin",
    "Counsel",
    "Meeting",
    "Validation",

    # API 문서화,
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'coronablue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coronablue.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'oilogezg',
        'USER' :'oilogezg',
        'PASSWORD' :'65VQ7POdSVURKffu9rkgA1Hhtdc61OgZ',
        'PORT':'5432',
        'HOST' : 'arjuna.db.elephantsql.com'
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]



# 지역설정 
TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'

# 기타 설정 
SITE_ID = 1 
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'

# setting avoid cors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Redis server
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",  # 1번 DB
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M",
}

