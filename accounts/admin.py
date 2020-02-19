from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from accounts.models import KakaoAccounts

admin.site.register(KakaoAccounts)

from django.contrib.sessions.models import Session


class SessionAdmin(ModelAdmin):
    # @staticmethod
    # def _session_data(self, obj):
    #     return obj.get_decoded()
    list_display = ['session_key', 'expire_date']


admin.site.register(Session, SessionAdmin)
