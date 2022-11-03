from rest_framework import serializers
from json import loads


def check_objs_order(objs, order_name='order'):
    orders = []
    if objs is None:
        return False
    for obj in objs:
        orders.append(obj[order_name])
    if len(set(orders)) != len(orders):
        raise serializers.ValidationError('存在描述为' + order_name + '的对象组中在无重复下不能明确的排序')


def check_objs_no_empty(objs, objs_name):
    if objs is not None:
        if len(objs) < 1:
            raise serializers.ValidationError(objs_name + '组的长度至少应为1')


def check_obj(obj_pk, OBJ):
    try:
        return OBJ.objects.get(obj_pk)
    except OBJ.DoesNotExist:
        raise serializers.ValidationError('存在名为' + str(OBJ) + '的模型类通过主键未找到对应的模型')

def check_change_duration(data, durantion_name):
    time_str = data.get(durantion_name)
    if time_str is None:
        return
    error_msg = "时长格式输入错误，请输入：{'y':[int],'m':[int],'d':[int],'h':[int]}"
    try:
        time = loads(time_str.replace("'", "\""))
        y = time.get('y') or 0
        m = time.get('m') or 0
        d = time.get('d') or 0
        h = time.get('h') or 0
        data[durantion_name] = '{' + '"y":{},"m":{},"d":{},"h":{}'.format(y, m, d, h) + '}'
        if y == 0 and m == 0 and d == 0 and h == 0:
            raise serializers.ValidationError(error_msg)
        if y < 0 or (m < 0 or m > 11) or (d < 0 or d > 29) or (h < 0 or h > 23):
            raise serializers.ValidationError(error_msg)
    except:
        raise serializers.ValidationError(error_msg)