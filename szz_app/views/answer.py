from rest_framework import generics, views, response, status
from szz_app.models import Answer
from szz_app.serializers import AnswerSerializer, AnswerWriteSerializer


class AnswerList(views.APIView):
    def get(self, request, format=None):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnswerWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerWriteSerializer
