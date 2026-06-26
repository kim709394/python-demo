""" 字典 dict 
字典是一种无序的集合，用于存储键值对。
key唯一，必须是不可变类型，如数字、字符串、元组等。int, str, tuple,float
类似java的map键值对
value可以是任意类型，包括可变类型，如列表、字典等。int, str, tuple,float
"""

# 定义dict
d1 = {"name": "bejamin", "age": 18, "gender": "male"}
print(d1) # {'name': 'bejamin', 'age': 18, 'gender': 'male'}
print(type(d1)) # <class 'dict'>

# 访问字典中的元素
print(d1["name"]) # bejamin
print(d1["age"]) # 18
print(d1["gender"]) # male

# 修改字典中的元素
d1["age"] = 19
print(d1) # {'name': 'bejamin', 'age': 19, 'gender': 'male'}

# 删除字典中的元素
del d1["age"]
print(d1) # {'name': 'bejamin', 'gender': 'male'}
d1.pop("gender")
print(d1) # {'name': 'bejamin'}

d1["age"]=20
d1["gender"]="male"
# 获取所有key值
print(d1.keys()) # dict_keys(['name', 'gender'])

# 获取所有value值
print(d1.values()) # dict_values(['bejamin', 'male'])

# 获取所有键值对
print(d1.items()) # dict_items([('name', 'bejamin'), ('gender', 'male')'])

# 遍历字典
for k,v in d1.items():
    print(k,v) # name bejamin gender male

for key in d1:
    print(key, d1[key]) # name bejamin gender male

# 获取字典的长度
print(len(d1)) # 2

# 清空字典
d1.clear()
print(d1) # {}


