from django.db import models

class QuestionnaireType(models.IntegerChoices):
    DEFAULT = 0, '无类型/通用类型'
    ELSE = 1, '其他'
    PSYCHOLOGY = 2, '心理学'
    PRIMARY_AND_SECONDARY_EDUCATION = 3, '中小学教育学'
    COLLEGE_STUDENT = 4, '大学生'
    SOCIAL_SURVEY = 5, '社会调查'
    PRODUCT_INQUIRY = 6, '产品调研'
    COVID19 = 7, '新冠有关'
    SATISFACTION_SURVER = 8, '满意度调查'
    MEASUREMENT = 9, '测评'
    TEST = 10, '考试'
    ONLINE_SHOPPING = 11, '网购'
    EMPLOYMENT_SITUATION = 12, '就业情况'
    HEALTH = 13, '健康'


class StateType(models.IntegerChoices):
    DEFAULT = 0, '原始状态'
    DEL = -1, '逻辑删除'
    ANONYMOUS = 1, '匿名'


class QuestionType(models.IntegerChoices):
    DEFAULT = 0, '无类型/通用类型'
    SOCIAL_HOT_SPOT = 1, '社会热点'
    PSYCHOLOGICAL = 2, '心理'
    CULTURE = 3, '文化'
    FILM_AND_TELEVISION = 4, '影视'
    MUSIC = 5, '音乐'
    SCIENCE_AND_TECHNOLOGY = 6, '科技'
    FINANCE_AND_ECONOMICS = 7, '财经'


class PlatformType(models.IntegerChoices):
    DEFAULT = 0, '本平台'
    WENJUANXING = 1, '问卷星'
    WENJUANWNAG = 2, '问卷网'
    TENGXUNDIAOCHA = 3, '腾讯调查'


class TopicType(models.IntegerChoices):
    REDIO = 0, '单选题'
    CHECKBOX = 1, '多选题'
    TEXT = 2, '文本题'
