from django.urls import path, re_path, include
from szz_app import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('questionnaire', views.QuestionnaireList.as_view()),
    path('questionnaire/<int:pk>', views.QuestionnaireDetail.as_view()),

    path('question', views.QuestionList.as_view()),
    path('question/<int:pk>', views.QuestionDetail.as_view()),

    path('answer', views.AnswerList.as_view()),
    path('answer/<int:pk>', views.AnswerDetail.as_view()),
    path('answerInQuestionPage/<int:question_id>', views.AnswerQuestionPageList.as_view()),

    path('userPage/<int:pk>', views.UserPageList.as_view()),
    path('userDetail/<int:pk>', views.UserDetail.as_view()),
    path('user', views.User.as_view()),

    path('result', views.ResultList.as_view())
    # path('question/<int:question_pk>/questionnaire', views.QuestionBindNairesList.as_view()),
    # path('question/<int:question_pk>/questionnaire/<int:questionnaire_pk>', views.QuestionBindNaireDetail.as_view())
]