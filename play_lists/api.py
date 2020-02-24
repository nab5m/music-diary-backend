from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from accounts.models import KakaoAccounts
from config.permissions import IsKakaoUser
from play_lists.models import PlayList
from play_lists.serializers import PlayListSerializer


class PlayListViewSet(viewsets.ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    permission_classes = [IsKakaoUser | permissions.IsAdminUser]

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_staff:
            return PlayList.objects.all()
        else:
            email = self.request.session.get('user_email')
            user = KakaoAccounts.objects.get(email=email)
            return PlayList.objects.filter(account=user)

    def perform_create(self, serializer):
        email = self.request.session.get('user_email')
        user = KakaoAccounts.objects.get(email=email)
        serializer.save(account=user)
