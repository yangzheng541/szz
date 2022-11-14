import django_filters
from django_filters.rest_framework import FilterSet
from ..models import Questionnaire

class QuestionnaireFilter(FilterSet):
    sort = django_filters.OrderingFilter(fields=('id',))
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')  # icontains，包含且忽略大小写
    user = django_filters.CharFilter(field_name='user')

    class Meta:
        model = Questionnaire
        fields = ['title', 'user']