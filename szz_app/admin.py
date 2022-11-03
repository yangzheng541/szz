from django.contrib import admin
from szz_app.models import UserInfo, Question, Answer, TakePoint, Questionnaire, Topic, Option, Result

# Register your models here.
admin.site.register([UserInfo, Question, Answer, TakePoint, Questionnaire, Topic, Option, Result])