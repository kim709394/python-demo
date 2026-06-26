""" 字符串操作方法 """
s = "hello-world"
print(s)

# 获取字符串里的字符
print(s[0]) # 正向索引 h
print(s[-1]) # 反向索引 d

# 切片
print(s[1:5]) # 从索引1开始，到索引5结束，不包含索引5
print(s[1:]) # 从索引1开始，到字符串结束
print(s[:5]) # 从字符串开始，到索引5结束，不包含索引5
print(s[1:5:2]) # 从索引1开始，到索引5结束，不包含索引5，步长为2
print(s[::-1]) # 字符串反转
print(s[-1:-7:-1]) # 字符串末位开始，到索引-7结束，不包含索引-7，步长为-1

# 常用方法
# find() 方法：返回子字符串首次出现的索引，如果不存在则返回 -1
print(s.find("w")) # 6
print(s.find("z")) # -1

# count() 方法：返回子字符串在字符串中出现的次数
print(s.count("l")) # 3
print(s.count("z")) # 0

# upper() 方法：将字符串转换为大写
print(s.upper()) # HELLO-WORLD

# lower() 方法：将字符串转换为小写
print(s.upper().lower()) # hello-world

# replace() 方法：将字符串中的子字符串替换为新的子字符串
print(s.replace("world","python")) # hello-python

# split() 方法：将字符串按指定分隔符分割成列表
print(s.split("-")) # ['hello', 'world']

# strip() 方法：移除字符串首尾的空格或指定字符
s1 = " "+s+" "
print(s1)
print(s1.strip()) # hello-world

# startswith() 方法：判断字符串是否以指定子字符串开头
print(s.startswith("hello")) # True
print(s.startswith("world")) # False

# endswith() 方法：判断字符串是否以指定子字符串结尾
print(s.endswith("world")) # True
print(s.endswith("hello")) # False
