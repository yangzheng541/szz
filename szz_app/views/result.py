from rest_framework import generics
from szz_app.serializers import ResultSerializer
from szz_app.models import Result


class ResultList(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = (ResultSerializer)
