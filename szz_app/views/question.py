from rest_framework import generics, response, views, status
from szz_app.models import Question
from szz_app.serializers import QuestionSerializer, QuestionWriteSerializer


class QuestionList(views.APIView):
    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionWriteSerializer
