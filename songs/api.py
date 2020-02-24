from rest_framework import permissions, generics
from rest_framework import filters

from config.permissions import IsKakaoUser
from songs.models import Song
from songs.serializers import SongSerializer


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'artist']
    permission_classes = [IsKakaoUser | permissions.IsAdminUser]


class SongDetailView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permissions_classes = [IsKakaoUser | permissions.IsAdminUser]
