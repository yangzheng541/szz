from django.contrib import admin
from szz_app.models import UserInfo, Question, Answer, TakePoint, Questionnaire, Topic, Option, Result, OptionResult, TextResult

# Register your models here.
admin.site.register([UserInfo, Question, Answer, TakePoint, Questionnaire, Topic, Option, Result, OptionResult, TextResult])