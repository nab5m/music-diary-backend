from django.contrib import admin

# Register your models here.
from accounts.models import KakaoAccounts, Token

admin.site.register(KakaoAccounts)
admin.site.register(Token)
