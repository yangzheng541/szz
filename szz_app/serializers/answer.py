from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Answer, TakePoint, Evidence
from .user import UserBasicSerializer
from szz_app.util import check_objs_order, check_objs_no_empty

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


class AnswerWriteSerializer(WritableNestedModelSerializer):
    takepoints = TakePointSerializer(many=True, required=False)
    class Meta:
        model = Answer
        fields = ('takepoints', 'body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state')

    def validate(self, data):
        takepoints = data['takepoints']
        check_objs_order(takepoints)
        check_objs_no_empty(takepoints, 'takepoints')
        self.force_default(data)
        return data

    def force_default(self, data):
        data['agree_count'] = 0
        data['look_count'] = 0
        data['share_count'] = 0
        data['state'] = 0


class AnswerSerializer(serializers.ModelSerializer):
    takepoints = TakePointSerializer(many=True, required=False)
    user = UserBasicSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = ('takepoints', 'body', 'agree_count', 'look_count', 'share_count', 'cover', 'user', 'create_time', 'state')
