from rest_framework import serializers
from szz_app.models import UserInfo, User


class UserInfoBasicSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)
    sex = serializers.BooleanField(read_only=True)
    birth = serializers.DateTimeField(read_only=True)
    class Meta:
        model = UserInfo
        fields = ('avatar', 'sex', 'birth')


class UserBasicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    userinfo = UserInfoBasicSerializer()
    class Meta:
        model = User
        fields = ('username', 'userinfo')
