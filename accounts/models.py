import random
import string
from datetime import datetime, timedelta

from django.db import models


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
