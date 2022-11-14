from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Topic, Questionnaire, Result, TopicResult, TextTypeResult, OptionTypeResult, User
from szz_app.util import TopicType
from .quesionnaire import QuestionnaireReadAllSerializer
from collections import OrderedDict

class TextTypeResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextTypeResult
        fields = ('id', 'answer')


class OptionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OptionTypeResult
        fields = ('id', 'answer')


class TopicResultSerializers(WritableNestedModelSerializer):
    text_type_result = TextTypeResultSerializers(required=False)
    option_type_result = OptionTypeSerializers(required=False, many=True)
    class Meta:
        model = TopicResult
        fields = ('id', 'text_type_result', 'option_type_result', 'topic')


class ResultSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=False)
    topic_result = TopicResultSerializers(required=False, many=True)
    class Meta:
        model = Result
        fields = '__all__'

    def validate(self, data):
        super().validate(data)
        self.force_default(data)
        print(data)
        return data

    def force_default(self, data):
        data['user'] = self.context['request'].user


class ResultUserPageSerializer(WritableNestedModelSerializer):
    questionnaire = QuestionnaireReadAllSerializer()
    class Meta:
        model = Result
        fields = ('questionnaire', )