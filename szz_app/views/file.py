from rest_framework import generics, permissions, views
from szz_app.serializers import PictureSerializer
from szz_app.models import Picture


class PictureList(generics.CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticated]
