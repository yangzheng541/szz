from rest_framework import generics, permissions, filters
from szz_app.serializers import ResultSerializer,ResultUserPageSerializer
from szz_app.models import Result
from szz_app.util import BasicPagination
from django_filters.rest_framework import DjangoFilterBackend


class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = (ResultSerializer)
    permission_classes = [permissions.IsAuthenticated]


class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = (ResultSerializer)
    permission_classes = [permissions.IsAuthenticated]

class ResultUserPage(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultUserPageSerializer
    pagination_class = BasicPagination
    permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filter_fields = ('user',)
    # ordering_fields = ('create_time',)

    def get_queryset(self):
        objects = Result.objects
        if self.request.query_params.get('user'):
            objects = objects.filter(user_id=self.request.query_params.get('user'))
        return objects.all()