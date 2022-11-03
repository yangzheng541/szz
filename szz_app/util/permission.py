from rest_framework import permissions, authentication

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它，读则无所谓
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class UserSelf(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它，读则无所谓
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    """
    关闭csrf验证
    """
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening