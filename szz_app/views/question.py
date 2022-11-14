from rest_framework import generics, permissions, status
from rest_framework.response import Response
from szz_app.util import IsOwnerOrReadOnly, BasicPagination
from szz_app.models import Question
from szz_app.serializers import QuestionReadSerializer, QuestionReadALLSerializer, QuestionCreateSerializer, QuestionUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    pagination_class = BasicPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = ('user', )
    ordering_fields = ('create_time', )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionReadALLSerializer
        elif self.request.method == 'POST':
            return QuestionCreateSerializer
        return None


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = ()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionReadSerializer
        elif self.request.method == 'POST':
            return QuestionUpdateSerializer
        return None
