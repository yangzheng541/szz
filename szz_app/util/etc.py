def del_key_value_s(data, del_keys):
    keys = [key for key in data.keys()]
    for key in keys:
        if key in del_keys and data.get(key):
            data.pop(key)

def destroy(obj):
    obj.state = -1
    obj.save()