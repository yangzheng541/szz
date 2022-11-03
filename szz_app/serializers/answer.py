from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Answer, TakePoint, Evidence
from .user import UserBasicSerializer
from szz_app.util import check_objs_order, check_objs_no_empty, del_key_value_s

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('order', 'data')


class TakePointSerializer(WritableNestedModelSerializer):
    evidences = EvidenceSerializer(many=True, required=True)
    class Meta:
        model = TakePoint
        fields = ('order', 'point', 'evidences')

    def validate(self, data):
        evidences = data['evidences']
        check_objs_order(evidences)
        check_objs_no_empty(evidences, 'evidences')
        return data


class AnswerBasicSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Answer
        fields = ('body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state')

    def force_default(self, data):
        pass


class AnswerWriteSerializer(AnswerBasicSerializer):
    takepoints = TakePointSerializer(many=True, required=False)
    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, data):
        check_objs_order(data.get('takepoints'))
        check_objs_no_empty(data.get('takepoints'), 'takepoints')
        self.force_default(data)
        return data

    def force_default(self, data):
        data['user'] = self.context['request'].user


class AnswerReadAllSerializer(AnswerBasicSerializer):
    user = UserBasicSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = ('body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state', 'question_title')


class AnswerReadSerializer(AnswerBasicSerializer):
    takepoints = TakePointSerializer(many=True, required=False)
    user = UserBasicSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = ('takepoints', 'body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time','state')


class AnswerCreateSerializer(AnswerWriteSerializer):
    def force_default(self, data):
        data['agree_count'] = 0
        data['look_count'] = 0
        data['share_count'] = 0
        data['state'] = 0


class AnswerUpdateSerializer(AnswerWriteSerializer):
    def force_default(self, data):
        del_keys = ['agree_count', 'look_count', 'share_count', 'state']
        del_key_value_s(data, del_keys)