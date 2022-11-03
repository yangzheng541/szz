from rest_framework import views, response, status
from rest_framework.authentication import BasicAuthentication
from szz_app.models import User as ModelUser, UserInfo
from django.contrib.auth.hashers import make_password
from szz_app.util import CsrfExemptSessionAuthentication

class User(views.APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = ()

    def post(self, request, format=None):
        r_data = request.data
        try:
            if r_data['password'] != r_data['repeat_password']:
                return response.Response({'error_msg': '两次输入密码不一致'}, status=status.HTTP_400_BAD_REQUEST)
            if ModelUser.objects.filter(username=r_data['username']):
                return response.Response({'error_msg': '用户名重复'}, status=status.HTTP_400_BAD_REQUEST)
            # Everything is ok:
            user = ModelUser.objects.create(username=r_data['username'], password=make_password(r_data['password']))
            return response.Response({'success_msg': '创建用户成功'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response({'error_msg': 'API给定参数错误，原错误消息为{}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
