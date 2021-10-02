import json
dict_a = {'k1': 'v1', 'k2': 'v2'}
# 将字典转化成json字符串
x = json.dumps(dict_a)
print(x)
print(type(x))
# 将json字符串转换成字典
y = json.loads(x)
print(y)
print(type(y))