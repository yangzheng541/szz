from rest_framework import serializers
from szz_app.models import Question
from .user import UserBasicSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()
    class Meta:
        model = Question
        fields = '__all__'


class QuestionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'