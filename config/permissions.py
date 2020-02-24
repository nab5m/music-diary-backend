from rest_framework import permissions, authentication

from accounts.views import KakaoAPI


class IsKakaoUser(permissions.BasePermission):
    # if test fails, raise PermissionDenied Exception

    def has_permission(self, request, view):
        if request.session.get('access_token', False):
            # ToDo: when token is expired, should refresh it
            return KakaoAPI.is_valid_token(request.session['access_token'])
        else:
            return False
