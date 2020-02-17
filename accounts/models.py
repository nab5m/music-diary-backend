import random
import string
from datetime import datetime, timedelta

from django.db import models

# Create your models here.


class Token(models.Model):
    account = models.OneToOneField('accounts.KakaoAccounts', on_delete=models.CASCADE, related_name="token"
                                   , blank=True, null=True)
    access_token = models.CharField(verbose_name="엑세스토큰", max_length=55, blank=False, null=False)
    expires_in = models.DateTimeField(verbose_name="엑세스토큰_만료시간", blank=True, null=True) # +12시간
    refresh_token = models.CharField(verbose_name="연장토큰", max_length=55, blank=True, null=True)
    refresh_token_expires_in = models.DateTimeField(verbose_name="연장토큰_만료시간", blank=True, null=True)    # +1개월 14일
    scope = models.CharField(verbose_name="조회범위", max_length=55, blank=True, null=True)

    class Meta:
        verbose_name = "토큰"
        verbose_name_plural = "토큰"

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.expires_in = now + timedelta(hours=6)
        self.refresh_token_expires_in = now + timedelta(days=45)
        super(Token, self).save(*args, **kwargs)


class KakaoAccounts(models.Model):
    class Meta:
        verbose_name = "카카오계정"
        verbose_name_plural = "카카오계정"

    kakao_id = models.TextField(verbose_name="카카오아이디", unique=True, blank=False, null=False)
    nickname = models.CharField(verbose_name="닉네임", max_length=50, blank=True, null=True)
    thumbnail_image = models.URLField(verbose_name="프사_URL", blank=True, null=True)
    email = models.EmailField(verbose_name="카카오계정이메일", blank=True, null=True)
    age_range = models.CharField(verbose_name="연령대", max_length=10, blank=True, null=True)
    gender = models.CharField(verbose_name="성별", max_length=6, blank=True, null=True)

    registerd_at = models.DateTimeField(verbose_name="가입날짜", auto_now_add=True)
