from django.contrib import admin
from django.contrib.admin import ModelAdmin

from songs.models import Song


class SongAdmin(ModelAdmin):
    list_display = ['title', 'artist']


admin.site.register(Song, SongAdmin)
