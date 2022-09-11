from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Questionnaire, Topic, Option
from .user import UserBasicSerializer
from szz_app.util import check_objs_order, check_objs_no_empty


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('label', 'content')


class TopicSerializer(WritableNestedModelSerializer):
    options = OptionSerializer(many=True, required=False)
    class Meta:
        model = Topic
        fields = ('title', 'order', 'description', 'type', 'options')


class QuestionnaireWriteSerializer(WritableNestedModelSerializer):
    topics = TopicSerializer(many=True, required=True)

    class Meta:
        model = Questionnaire
        fields = ('title', 'description', 'user', 'topics')

    def validate(self, data):
        topics = data['topics']
        self.check_topics(topics)
        self.force_default(data)
        return data

    def type2chr(self, type):
        topic_type = ['单选题', '多选题', '文本题']
        if type > len(topic_type) - 1:
            return None
        else:
            return topic_type[type]

    def check_topics(self, topics):
        check_objs_no_empty(topics, 'topics')  # 保证题目组的长度至少为1
        check_objs_order(topics)  # 保证题目有序
        for topic in topics:
            self.check_topic_type(topic)  # 保证题目类型符合条件
            check_objs_order(topic.get('options'), 'label')  # 保证选项有序

    def check_topic_type(self, topic):
        type_chr = self.type2chr(topic['type'])
        if type_chr is None:  # 非有效类型
            return False
        if type_chr == '单选题' or type_chr == '多选题':
            if topic.get('options') is None:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options为空')
            if len(topic['options']) < 2:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options的长度小于2')
        elif type_chr == '文本题':
            if topic.get('options') is not None:
                raise serializers.ValidationError(topic['title'] + '为选择题，但其options为非空')
            if topic['description'].strip() == '':
                raise serializers.ValidationError(topic['title'] + '为文本题，但其desciption为空字符串')

    def force_default(self, data):
        data['state'] = 0


class QuestionnaireSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, required=True)
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = Questionnaire
        fields = ('title', 'description', 'user', 'topics')
