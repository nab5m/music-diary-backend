from rest_framework import serializers

from play_lists.models import PlayList
from songs.serializers import SongSerializer


class PlayListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayList
        fields = [
            "id",
            "account",
            "title",
            "songs",

            "created",
            "last_updated",
        ]
        extra_kwargs = {'account': {'required': False}, 'songs': {'required': False}}
