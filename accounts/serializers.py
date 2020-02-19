from rest_framework import serializers
from accounts.models import KakaoAccounts


class KakaoAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = KakaoAccounts
        fields = ['id', 'kakao_id', 'nickname', 'thumbnail_image', 'email', 'age_range', 'gender', 'token']
