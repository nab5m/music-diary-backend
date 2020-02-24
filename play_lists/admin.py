from django.contrib import admin

from play_lists.models import PlayList

# ToDo: need update for songs(ManyToManyField) in admin interface
admin.site.register(PlayList)
