from rest_framework import views, response, status
from rest_framework.authentication import BasicAuthentication
from szz_app.models import User as ModelUser, UserInfo
from django.contrib.auth.hashers import make_password
from szz_app.util import CsrfExemptSessionAuthentication, UserSelf
from django.http import Http404

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
            UserInfo.objects.create(user=user)
            return response.Response({'success_msg': '创建用户成功'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response({'error_msg': 'API给定参数错误，原错误消息为{}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)

class PasswordDetail(views.APIView):
    permission_classes = [UserSelf]

    def get_object(self, pk):
        try:
            return ModelUser.objects.get(id=pk)
        except ModelUser.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if old_password is not None and new_password is not None and user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return response.Response({'success_msg': '修改密码成功'}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({'err_msg': '密码格式存在错误'}, status=status.HTTP_400_BAD_REQUEST)
