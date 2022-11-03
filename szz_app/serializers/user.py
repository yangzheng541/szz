from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import UserInfo, User


class UserInfoBasicSerializer(WritableNestedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('avatar', )


class UserBasicSerializer(WritableNestedModelSerializer):
    userinfo = UserInfoBasicSerializer()
    class Meta:
        model = User
        fields = ('username', 'userinfo')


class UserInfoPageSerializer(WritableNestedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'avatar', 'sex', 'birth', 'job', 'address', 'phone',
                  'fans_count', 'attentions_count', 'questions_count', 'answers_count')


class UserPageSerializer(WritableNestedModelSerializer):
    userinfo = UserInfoPageSerializer()
    class Meta:
        model = User
        fields = ('username', 'userinfo', 'email')

