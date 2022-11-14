from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Questionnaire, Topic, Option, Question
from .user import UserBasicSerializer
from szz_app.util import check_objs_order, check_objs_no_empty, check_change_duration, \
                         del_key_value_s, TopicType
from json import loads
from datetime import datetime, timezone, timedelta
from collections import OrderedDict


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('label', 'content')


class TopicSerializer(WritableNestedModelSerializer):
    options = OptionSerializer(many=True, required=False)
    class Meta:
        model = Topic
        fields = ('id', 'title', 'order', 'description', 'type', 'options', 'required', 'has_other', 'max_select')


class QuestionnaireBaseSerializer(WritableNestedModelSerializer):
    topics = TopicSerializer(many=True, required=True)

    class Meta:
        model = Questionnaire
        fields = '__all__'


class QuestionnaireReadSerializer(QuestionnaireBaseSerializer):
    user = UserBasicSerializer(read_only=True)


class QuestionnaireReadAllSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)  # 没有题目详细细节，当get所有时

    class Meta:
        model = Questionnaire
        fields = '__all__'


class QuestionnaireWriteSerializer(QuestionnaireBaseSerializer):
    def validate(self, data):
        self.check_topics(data['topics'])
        self.check_end_time(data.get('end_time'))
        check_change_duration(data, 'fill_time')
        self.force_default(data)
        return data

    def check_topics(self, topics):
        check_objs_no_empty(topics, 'topics')  # 保证题目组的长度至少为1
        check_objs_order(topics)  # 保证题目有序
        for topic in topics:
            self.check_topic_type(topic)  # 保证题目类型符合条件
            check_objs_order(topic.get('options'), 'label')  # 保证选项有序

    def check_end_time(self, end_time):
        if end_time is not None and datetime.now() > end_time:
            raise serializers.ValidationError('问卷起始时间小于终止时间')

    def check_topic_type(self, topic):
        if topic['type'] in [TopicType.REDIO, TopicType.CHECKBOX]:
            if topic.get('options') is None:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options为空')
            if len(topic['options']) < 2:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options的长度小于2')
            # ---- 多选
            self.check_muti_type(topic)
        elif topic['type'] in [TopicType.TEXT]:
            if topic.get('options') is not None and len(topic.get('options')) != 0:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options为非空')
            if topic['description'].strip() == '':
                raise serializers.ValidationError(topic['title'] + '为文本题，但其desciption为空字符串')

    def check_muti_type(self, topic):
        if topic['type'] == TopicType.CHECKBOX:
            if topic.get('has_other') is None or topic.get('max_select') is None:
                raise serializers.ValidationError(topic['title'] + '为多选题，但最多选择或其他项为空')
        else:
            if topic.get('max_select') is not None or topic.get('max_select') is not None:
                raise serializers.ValidationError(topic['title'] + '为单选题，但最多选择或其他项为非空')

    def force_default(self, data):
        data['user'] = self.context['request'].user


class QuestionnaireCreateSerializer(QuestionnaireWriteSerializer):
    def force_default(self, data):
        super().force_default(data)
        data['fill_count'] = 0  # 强制要求初始化为0
        data['share_count'] = 0
        data['recommend_count'] = 0
        data['state'] = 0
        data['create_time'] = datetime.now()


class QuestionnaireUpdateSerializer(QuestionnaireWriteSerializer):
    def force_default(self, data):
        super().force_default(data)
        del_keys = ['create_time', 'fill_count', 'share_count', 'recommend_count', 'state']
        del_key_value_s(data, del_keys)


class QuestionnaireResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('its_result', )
