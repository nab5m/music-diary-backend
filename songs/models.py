from django.db import models


class Song(models.Model):
    class Meta:
        verbose_name = "노래"
        verbose_name_plural = "노래"

    def __str__(self):
        return self.title + " <%s>" % self.artist

    title = models.CharField("노래 제목", max_length=255)
    thumbnail_image_url = models.URLField("썸네일 이미지 주소", blank=True, null=True)
    artist = models.CharField("가수", max_length=255)
