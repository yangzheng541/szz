from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Question, Questionnaire, Answer
from .user import UserBasicSerializer
from .quesionnaire import QuestionnaireReadSerializer
from szz_app.util import check_obj, del_key_value_s


# 编写纪录一：多对多字段在写中不会显露（'__all__'情况下）
# 编写纪录二：当存在展示时可以关联列出来（user的相关字段），但是不可写入（只可写入id），可分为两个序列化器写
# 编写纪录三：model中的自定义属性需要显式引用才可使用（'__all__'不行）


class QuestionBaseSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def validate(self, data):
        self.force_default(data)
        return data

    def force_default(self, data):
        pass


class QuestionReadALLSerializer(QuestionBaseSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'look_count', 'share_count', 'create_time', 'type', 'state',
                  'questionnaires_len', 'answers_abouts')


class QuestionReadSerializer(QuestionBaseSerializer):
    user = UserBasicSerializer(read_only=True)
    questionnaires = QuestionnaireReadSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'look_count', 'share_count', 'create_time', 'type', 'state',
                  'questionnaires', 'user')


class QuestionWriteSerializer(QuestionBaseSerializer):
    questionnaires = serializers.PrimaryKeyRelatedField(queryset=Questionnaire.objects.all(), many=True, required=False)

    def force_default(self, data):
        data['user'] = self.context['request'].user
        # 写操作必须保持用户为当前用户（对于POST方法，这是对用户只能创建属于自己的问卷的保证；对于PUT方法，这是保证用户不能将自己的问卷更改为其他用户的）


class QuestionCreateSerializer(QuestionWriteSerializer):
    def force_default(self, data):
        super().force_default(data)
        data['state'] = 0
        data['look_count'] = 0
        data['share_count'] = 0
        # 初始化时默认状态为0，两个数均初始化为0


class QuestionUpdateSerializer(QuestionWriteSerializer):
    def force_default(self, data):
        super().force_default(data)
        del_key = ['state', 'look_count', 'share_count']
        del_key_value_s(data, del_key)
        # 去除look_count、share_count两属性，不能通过更新修改这两个字段
