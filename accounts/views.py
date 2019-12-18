from django.shortcuts import render, redirect
import requests
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Token
from config.secret_settings import KAKAO_REST_APP_KEY
from config.settings import KAKAO_REDIRECT_URI


class IndexView(TemplateView):
    template_name = 'index.html'


@api_view(['GET'])
def request_login_url(request):
    token = None
    if 'device_token' in request.GET:
        token = Token.objects.filter(device_token=request.GET['device_token'])
    else:
        token = Token.create()
        token.save()

    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    login_request_uri += 'client_id=' + KAKAO_REST_APP_KEY
    login_request_uri += '&redirect_uri=' + KAKAO_REDIRECT_URI
    login_request_uri += '&response_type=code'

    return Response({'login_request_uri': login_request_uri, 'device_token': token.device_token})
    # return render(request, 'accounts/index.html', {})


def oauth(request):
    code = request.GET['code']

    access_token_request_uri = 'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&'

    access_token_request_uri += 'client_id=' + KAKAO_REST_APP_KEY
    access_token_request_uri += '&redirect_uri=' + KAKAO_REDIRECT_URI
    access_token_request_uri += '&code=' + code

    # 엑세스 토큰 요청
    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()

    # 엑세스 토큰 수신 성공
    if 'access_token' in json_data:
        access_token = json_data['access_token']

        user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"

        headers = {'Authorization': 'Bearer ' + access_token}
        data = {
            'property_keys': ['kakao_account.profile',
                              'kakao_account.email',
                              'kakao_account.age_range',
                              'kakao_account.gender'],
        }
        user_profile_info_uri_data = requests.get(user_profile_info_uri, headers=headers)
        user_json_data = user_profile_info_uri_data.json()

        print(user_json_data)
    else:
        print('error oauth')

    return redirect('http://localhost:8000/index/')
