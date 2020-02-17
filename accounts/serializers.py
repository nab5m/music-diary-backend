from rest_framework import serializers
from accounts.models import KakaoAccounts, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'access_token', 'expires_in', 'refresh_token', 'refresh_token_expires_in', 'scope', 'token']


class KakaoAccountSerializer(serializers.ModelSerializer):
    token = TokenSerializer()

    class Meta:
        model = KakaoAccounts
        fields = ['id', 'kakao_id', 'nickname', 'thumbnail_image', 'email', 'age_range', 'gender', 'token']
