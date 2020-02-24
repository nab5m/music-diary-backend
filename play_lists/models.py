from django.db import models

from accounts.models import KakaoAccounts


class PlayList(models.Model):
    class Meta:
        verbose_name = "플레이 리스트"
        verbose_name_plural = "플레이 리스트"

    def __str__(self):
        return self.title + " <%s - %s>" % (self.account.nickname, self.account.email)

    account = models.ForeignKey('accounts.KakaoAccounts', on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=255)
    songs = models.ManyToManyField('songs.Song', blank=True)

    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
