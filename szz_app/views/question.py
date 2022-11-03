from rest_framework import generics, permissions, status
from rest_framework.response import Response
from szz_app.util import IsOwnerOrReadOnly, BasicPagination
from szz_app.models import Question
from szz_app.serializers import QuestionReadSerializer, QuestionReadALLSerializer, QuestionCreateSerializer, QuestionUpdateSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    pagination_class = BasicPagination
    permission_classes = [permissions.IsAuthenticated]

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
