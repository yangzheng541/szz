from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserInfo(models.Model):
    # User用的是Django自带的auth_user的模型：其中已包含用户名（唯一）、密码、邮箱，这里将它拓展
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    avatar = models.ImageField(upload_to='avatar', default='', verbose_name='头像')
    sex = models.BooleanField(null=True)
    birth = models.DateTimeField(null=True, blank=True)
    job = models.IntegerField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=128)
    phone = models.CharField(null=True, blank=True, max_length=16)
    fans = models.ManyToManyField('UserInfo', blank=True)  # 关注-粉丝是多对多表


class Question(models.Model):
    # 问题模型（区分问卷模型）
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    look_count = models.IntegerField(default=0)  # 查看数（在获取问题api中，每获取一次问题数据时，令此项加一）
    share_count = models.IntegerField(default=0)  # 分享数（应有一专门api增长分享数）
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)  # 0正常 | 1匿名问题 | 2逻辑删除


class Answer(models.Model):
    # 回答数据（与问题模型相对应）（是一对多关系）
    body = models.TextField(null=True, blank=True)  # 除去论点论据外的其他回答部分
    agree_count = models.IntegerField(default=0)  # 点赞数（应有一专门api增长点赞数）
    look_count = models.IntegerField(default=0)  # 查看数（在获取问题api中，每获取一次问题数据时，令此项加一）
    share_count = models.IntegerField(default=0)  # 分享数（应有一专门api增长分享数）
    cover = models.ImageField(upload_to='cover', default='', verbose_name='封面')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)  # 0正常 | 1匿名回答 | 2逻辑删除


class TakePoint(models.Model):
    # 论点-论据模型（一个回答下可以有多个论点和论据）
    order = models.IntegerField()  # 论点的次序
    point = models.CharField(max_length=255)  # 只能以文字形式
    data = models.TextField()  # 可通过富文本形式（存储为富文本）
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)


class Questionnaire(models.Model):
    # 问卷模型（问卷和问题是多对多的关系）
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)  # 0正常 | 1匿名问卷 | 2逻辑删除


class Topic(models.Model):
    # 题目模型（与问卷模型是多对一关系）
    title = models.CharField(max_length=255)
    order = models.IntegerField()  # 题目的次序
    description = models.TextField(null=True, blank=True)
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
