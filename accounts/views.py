from datetime import datetime, timedelta

from django.shortcuts import render, redirect
import requests
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Token, KakaoAccounts
from config.secret_settings import KAKAO_REST_APP_KEY
from config.settings import KAKAO_REDIRECT_URI


class IndexView(TemplateView):
    template_name = 'index.html'


@api_view(['GET'])
def request_login_url(request):
    # 카카오 로그인 url을 보내줌
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

    login_request_uri += 'client_id=' + KAKAO_REST_APP_KEY
    login_request_uri += '&redirect_uri=' + KAKAO_REDIRECT_URI
    login_request_uri += '&response_type=code'

    return Response({'login_request_uri': login_request_uri})


class KakaoAPI:
    user_profile_info_uri = "https://kapi.kakao.com/v2/user/me"

    access_token_request_uri = 'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&'
    access_token_request_uri += 'client_id=' + KAKAO_REST_APP_KEY
    access_token_request_uri += '&redirect_uri=' + KAKAO_REDIRECT_URI

    @classmethod
    def get_access_token_json(cls, code):
        access_token_request_uri = cls.access_token_request_uri + '&code=' + code

        # 엑세스 토큰 요청
        access_token_request_uri_data = requests.get(access_token_request_uri)
        return access_token_request_uri_data.json()

    @classmethod
    def get_user_profile(cls, access_token):
        headers = {'Authorization': 'Bearer ' + access_token}

        # 프로필 조회 요청
        user_profile_info_uri_data = requests.get(cls.user_profile_info_uri, headers=headers)
        return user_profile_info_uri_data.json()

    @classmethod
    def register_music_diary(cls, user_json_data):
        account_data = user_json_data['kakao_account']
        account = KakaoAccounts(kakao_id=user_json_data['id'])

        if account_data['has_email'] and not account_data['email_needs_agreement']:
            account.email = account_data['email']
        if account_data['has_age_range'] and not account_data['age_range_needs_agreement']:
            account.age_range = account_data['age_range']
        if account_data['has_gender'] and not account_data['gender_needs_agreement']:
            account.gender = account_data['gender']

        account.nickname = user_json_data['properties']['nickname']
        account.thumbnail_image = user_json_data['properties']['thumbnail_image']

        account.save()
        return account

# ToDo: 함수가 길어
@api_view(['GET'])
def oauth(request):
    code = request.GET['code']
    token = None
    result = None

    json_data = KakaoAPI.get_access_token_json(code)

    # 엑세스 토큰 수신 성공
    if 'access_token' in json_data:
        access_token = json_data['access_token']
        refresh_token = json_data['refresh_token']
        scope = json_data['scope']

        user_json_data = KakaoAPI.get_user_profile(access_token)

        # 프로필 조회 성공
        if 'id' in user_json_data:
            account_query = KakaoAccounts.objects.filter(kakao_id=user_json_data['id'])
            account = None

            if len(account_query) == 1:
                account = account_query.get()

            # 첫 로그인
            elif len(account_query) == 0:
                account = KakaoAPI.register_music_diary(user_json_data)

            # 기존 토큰 있으면 지움
            # ToDo: 기존 토큰 있으면 유효기간 검사하고 갱신하는 방향으로 수정
            try:
                token = account.token
                token.delete()
            except (KakaoAccounts.token.RelatedObjectDoesNotExist, AttributeError):
                pass

            # save new Token
            token = Token(
                account=account,
                access_token=access_token,
                refresh_token=refresh_token,
                scope=scope
            )
            token.save()

            account.token = token
            account.save()

        result = {'id': user_json_data['id']}

    # 엑세스 토큰 수신 실패
    else:
        result = {'error': "can't get access_token"}

    return Response(result)


@api_view(['GET'])
def user_detail(request, id):
    # DoesNotExist exception
    print(id)
    account = KakaoAccounts.objects.get(kakao_id=id)

    return Response()
