from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import UserInfo, User
from szz_app.util.serializer_field import Base64ImageField


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
    avatar = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = UserInfo
        fields = ('id', 'avatar', 'sex', 'birth', 'job', 'address', 'phone',
                  'fans_count', 'attentions_count', 'questions_count', 'answers_count',
                  'questionnaire_count', 'fill_questionnaire_count')


class UserPageSerializer(WritableNestedModelSerializer):
    userinfo = UserInfoPageSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'userinfo', 'email', 'date_joined')

    def validate(self, data):
        self.force_default(data)
        return data

    def force_default(self, data):
        data['id'] = self.context['request'].user.id
