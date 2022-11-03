from rest_framework import generics, views, response, status, permissions
from szz_app.models import Answer
from szz_app.serializers import AnswerReadAllSerializer, AnswerCreateSerializer, AnswerReadSerializer, AnswerUpdateSerializer
from szz_app.util import BasicPagination


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    pagination_class = BasicPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnswerReadAllSerializer
        else:
            return AnswerCreateSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnswerReadSerializer
        else:
            return AnswerUpdateSerializer


class AnswerQuestionPageList(generics.ListAPIView):
    pagination_class = BasicPagination
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, question_id, format=None):
        answers = Answer.objects.filter()
        serializer = AnswerReadSerializer(answers, many=True)
        return response.Response(serializer.data)
