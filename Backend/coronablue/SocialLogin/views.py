from django.shortcuts import render

# HTTP MODULE
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured

# DRF MODULE
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView

# Inner app
from User.models import User

# for call server
import urllib
import requests
import os
import json

with open("env.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# 카카오


def kakao_login(request):
    if request.method == 'GET':
        print("들어옴?")
        app_rest_api_key = get_secret("KAKAO_RESTAPI_KEY")
        redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
        # print(redirect_uri)
        return JsonResponse({"url": "https://kauth.kakao.com/oauth/authorize?client_id="+app_rest_api_key+"&redirect_uri="+redirect_uri+"&response_type=code"}, status=200)
        # return redirect( f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code")

# access token 요청


def kakao_callback(request):
    app_rest_api_key = get_secret("KAKAO_RESTAPI_KEY")
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
    user_token = request.GET.get("code")
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}")

    token_response_json = token_request.json()
    print(token_response_json)
    error = token_response_json.get("error", None)

    # if there is an error from token_request
    if error is not None:
        raise RuntimeError()
    access_token = token_response_json.get("access_token")

    return redirect(f"http://localhost:8080/kakaocheck?access_token={access_token}")


@csrf_exempt
def kakao_login_check(request):
    if request.method == "POST":
        # 수정해야할 부분
        print("들어옴??@22222")
        access_token = JSONParser().parse(request)['access_token']

        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        print(profile_json)
        kakao_account = profile_json.get("kakao_account")
        # 필수 항목 4 가지
        userimg = str(kakao_account.get("profile").get("profile_image_url"))
        name = str(kakao_account.get("profile").get("nickname"))
        email = str(kakao_account.get("email"))
        id = int(profile_json.get("id"))
        print(id)
        social = User.objects.filter(issocial=id)
        print(social)
        if len(list(social)) > 0:
            return JsonResponse({"data": dict(social.values()[0])}, status=200)
        else:
            return JsonResponse({'name': name, "link": False, "id": id, "message": "id를 isSocail 값으로 넘겨주세요"}, status=200)


# 페이스북


# 구글

def google_login(request):
    print("여기에 왔다~!")
    app_rest_api_key = get_secret("KAKAO_RESTAPI_KEY")
    redirect_uri = "http://127.0.0.1:8000/account/login/kakao/callback/"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code")


def google_callback(request):
    print("여기에 왔다!")

    return JsonResponse({'name': "12"}, status=200)
