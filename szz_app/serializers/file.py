from rest_framework import serializers
from ..models import Picture, User
from szz_app.util import Base64ImageField


class PictureSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    picture = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = Picture
        fields = '__all__'

    def validate(self, data):
        self.force_default(data)
        return data

    def force_default(self, data):
        data['user'] = self.context['request'].user
