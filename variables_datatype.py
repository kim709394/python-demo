""" 变量和数据类型 """
# 注释语法
# hello world
print("hello world")
""" 这是一个多行注释
    数据类型
"""

# 字符串,可以用单引号也可以用双引号
a = "hello world"
b = 'hello world'
c = "I'm back"

# 字符串可以包含特殊字符，如换行符、制表符等,\t空格，\n换行符
d = "\thello\nworld"
print(d)

# 字符串可以包含转义字符，如反斜杠、引号等
e = "hello\\world\""
print(e)

# 字符串拼接
print(a+b+c)
s1 = "我是" "一个" "球王"
print(s1)

# 字符串和数字可以拼接，但是数字必须转换为字符串
print(a+str(100))

# 多行字符串
d = """
line1
line2
line3
"""
print(d)

# 字符串的格式化
a="C罗"
b = 41
c ="一个球王"
s2 = "我是%s,我今年%s岁,我是%s" % (a,b,c)   #方法1
print(s2)
s2 = f"我是{a},我今年{b}岁,我是{c}"   #方法2,推荐使用方法二
print(s2)

# 整数
print(10)

# 浮点数
print(10.9)

# 布尔值
print(False)
print(True)

# 布尔值本质上也是整数，False等于0，True等于1
print(False == 0);  print(False+1) # 1
print(True == 1);  print(True+1) # 2

# None,空值
print(None)

""" 
    变量，python是解释性语言，变量是弱类型的，变量的类型是根据赋值的值来确定的，
    变量可以是整数、浮点数、布尔值、字符串、元组、列表、字典、集合等。
 """
num = 100
num = "hello world"
num = True

# 一次性定义多个变量
a, b, c = 1, 2.3, 3.5
print(a, b, c)

#标识符
true = 1
print(true)
