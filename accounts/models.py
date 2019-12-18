import random
import string

from django.db import models

# Create your models here.


class Token(models.Model):
    device_token = models.CharField(verbose_name="디바이스토큰", max_length=55, blank=False, null=False)
    access_token = models.CharField(verbose_name="엑세스토큰", max_length=55, blank=True, null=True)
    expires_in = models.DateTimeField(verbose_name="엑세스토큰_만료시간", blank=True, null=True)
    refresh_token = models.CharField(verbose_name="연장토큰", max_length=55, blank=True, null=True)
    refresh_token_expires_in = models.DateTimeField(verbose_name="연장토큰_만료시간", blank=True, null=True)
    scope = models.CharField(verbose_name="조회범위", max_length=55, blank=True, null=True)

    class Meta:
        verbose_name = "토큰"
        verbose_name_plural = "토큰"

    @classmethod
    def random_string_digits(cls, length=50):
        """Generate a random string of letters and digits """
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))

    @classmethod
    def is_device_token_unique(cls, token):
        if len(cls.objects.filter(device_token=token)):
            return False
        else:
            return True
    @classmethod
    def create(cls):
        while True:
            random_string = cls.random_string_digits()
            if cls.is_device_token_unique(random_string):
                break

        token = cls(device_token=random_string)
        return token


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
