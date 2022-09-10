from rest_framework import generics, views, response, status
from szz_app.models import Questionnaire, Topic, Option
from szz_app.serializers import QuestionnaireSerializer, TopicSerializer, OptionSerializer, QuestionnaireWriteSerializer


class QuestionnaireList(views.APIView):
    def get(self, request, format=None):
        questionnaire = Questionnaire.objects.all()
        serializer = QuestionnaireSerializer(questionnaire, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionnaireWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionnaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireWriteSerializer
