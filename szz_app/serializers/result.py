from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from szz_app.models import Topic, Questionnaire, Result, TopicResult, TextTypeResult, OptionTypeResult
from szz_app.util import TopicType
from collections import OrderedDict

class TextTypeResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextTypeResult
        fields = ('answer', )


class OptionTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = OptionTypeResult
        fields = ('answer', )


class TopicResultSerializers(WritableNestedModelSerializer):
    text_type_result = TextTypeResultSerializers(required=False)
    option_type_result = OptionTypeSerializers(required=False)
    answer = serializers.CharField(required=False)
    class Meta:
        model = TopicResult
        fields = ('text_type_result', 'option_type_result', 'topic', 'answer')

    @property
    def corresponding(self):
        return {
            'option_type_result': [TopicType.REDIO, TopicType.CHECKBOX],
            'text_type_result': [TopicType.TEXT]
        }

    def validate(self, data):
        self.verify_result_type(data)
        print(data)
        return data

    def verify_result_type(self, data):
        topic = data['topic']
        for tr_name, c_type in self.corresponding.items():
            if topic.type in c_type:
                if data.get('answer') is None:
                    raise serializers.ValidationError('xx_result（某种类型的结果）与其topic所对应的类型不一致')
                else:
                    data[tr_name] = OrderedDict(answer=data['answer'])
                    data.pop('answer')
                    return


class ResultSerializer(WritableNestedModelSerializer):
    topic_result = TopicResultSerializers(required=False, many=True)
    class Meta:
        model = Result
        fields = ('questionnaire', 'user', 'create_time', 'topic_result')

    # 总的来看
    # 每道选择题下的情况：选择A选项的人有多少...选择B选项的人有多少...以此类推
    # 每道文本题下的情况：给一个链接，可以下载所有的填写情况
        # 返回一个词云图
    # 每道题下的

    # 分开来看每个问卷的答案