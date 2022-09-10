from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Answer, TakePoint
from .user import UserBasicSerializer

class TakePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakePoint
        fields = ('order', 'point', 'data')


class AnswerWriteSerializer(WritableNestedModelSerializer):
    takepoint = TakePointSerializer(required=False)
    class Meta:
        model = Answer
        fields = ('takepoint', 'body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state')


class AnswerSerializer(serializers.ModelSerializer):
    takepoint = TakePointSerializer(required=False)
    user = UserBasicSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = ('takepoint', 'body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state')
