from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# 编写原则一：使用null=True时，必须尽量使用默认值（大多数情况下，选项、图片类字段不可带默认值）
# 编写原则二：如果需要强行规定默认值——必须不可改时，则在序列化类拓展force_default方法
# 编写原则三：不使用blank=True，序列化器尽可识别null=True的项可以在参数选择中不出现
# 编写原则四：非null=True，则为必须提交的字段

class UserInfo(models.Model):
    # User用的是Django自带的auth_user的模型：其中已包含用户名（唯一）、密码、邮箱，这里将它拓展
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    avatar = models.ImageField(upload_to='avatar', default='', verbose_name='头像')
    sex = models.BooleanField(null=True)
    birth = models.DateTimeField(null=True)
    job = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=128, default='')
    phone = models.CharField(null=True, max_length=16, default='')
    fans = models.ManyToManyField('UserInfo')  # 关注-粉丝是多对多表


class Question(models.Model):
    # 问题模型（区分问卷模型）
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, default='')
    look_count = models.IntegerField(null=True, default=0)  # 查看数（在获取问题api中，每获取一次问题数据时，令此项加一）
    share_count = models.IntegerField(null=True, default=0)  # 分享数（应有一专门api增长分享数）
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(null=True, default=0)  # 0正常 | 1匿名问题 | 2逻辑删除


class Answer(models.Model):
    # 回答数据（与问题模型相对应）（是一对多关系）
    body = models.TextField(null=True, default=0)  # 除去论点论据外的其他回答部分
    agree_count = models.IntegerField(default=0, null=True)  # 点赞数（应有一专门api增长点赞数）
    look_count = models.IntegerField(default=0, null=True)  # 查看数（在获取问题api中，每获取一次问题数据时，令此项加一）
    share_count = models.IntegerField(default=0, null=True)  # 分享数（应有一专门api增长分享数）
    cover = models.ImageField(upload_to='cover', verbose_name='封面', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0, null=True)  # 0正常 | 1匿名回答 | 2逻辑删除


class TakePoint(models.Model):
    # 论点模型（一个回答下可以有多个论点）
    order = models.IntegerField()  # 论点的次序
    point = models.CharField(max_length=255)  # 只能以文字形式
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='takepoints')


class Evidence(models.Model):
    # 论据模型（关于一个论点可以有多个论据）
    order = models.IntegerField()  # 论据的次序
    data = models.TextField()  # 可通过富文本形式（存储为富文本）
    takepoint = models.ForeignKey('TakePoint', on_delete=models.CASCADE, related_name='evidences')


class Questionnaire(models.Model):
    # 问卷模型（问卷和问题是多对多的关系）
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(null=True, default=0)  # 0正常 | 1匿名问卷 | 2逻辑删除


class Topic(models.Model):
    # 题目模型（与问卷模型是多对一关系）
    title = models.CharField(max_length=255)
    order = models.IntegerField()  # 题目的次序
    required = models.BooleanField()  # 必答题和选答题
    description = models.TextField(null=True, default='')
    type = models.IntegerField()  # 单选题、多选题、文本题（基本题型）
    questionare = models.ForeignKey('Questionnaire', on_delete=models.CASCADE, related_name='topics')


class Option(models.Model):
    # 选择题模型（与题目模型多对一关系）
    label = models.IntegerField()  # 0 = A，以此类推
    content = models.TextField()
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='options')


class Result(models.Model):
    # 问卷结果模型（与问卷模型多对一）
    answer = models.TextField()  # 文本题->文本答案 | 选择题->选项（数字形式）
    questionnaire = models.ForeignKey('Questionnaire', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)


class OptionResult(models.Model):
    # 选择题结果模型（与结果模型多对一）
    label = models.IntegerField()  # 选择题的结果，0 = A，以此类推
    result = models.ForeignKey('Result', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)


class TextResult(models.Model):
    # 文本题结果模型（与结果模型多对一）
    content = models.TextField()  # 文本题的结果
    result = models.ForeignKey('Result', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
