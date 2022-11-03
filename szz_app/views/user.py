from rest_framework import generics, permissions
from szz_app.serializers import UserPageSerializer
from szz_app.models import User
from szz_app.util import UserSelf

class UserPageList(generics.RetrieveAPIView):
    queryset = User
    serializer_class = UserPageSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User
    serializer_class = UserPageSerializer
    permission_classes = [UserSelf]
