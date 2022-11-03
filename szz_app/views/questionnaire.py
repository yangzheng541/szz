from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from szz_app.util import IsOwnerOrReadOnly, destroy, BasicPagination
from szz_app.models import Questionnaire
from szz_app.serializers import QuestionnaireUpdateSerializer, QuestionnaireReadSerializer, \
    QuestionnaireReadAllSerializer, QuestionnaireCreateSerializer


class QuestionnaireList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = BasicPagination
    filterset_fields = ['title', 'type', ]
    ordering_fields = ('title', 'fill_time', 'create_time', 'fill_money', )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionnaireReadAllSerializer
        elif self.request.method == 'POST':
            return QuestionnaireCreateSerializer
        return None


class QuestionnaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionnaireReadSerializer
        else:
            return QuestionnaireUpdateSerializer
