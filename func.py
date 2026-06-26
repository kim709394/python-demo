""" 函数 """
# 全局变量，函数内外部都可以访问
global_var = "nonado"

# 定义函数
def print_hello():
    print(f"hello,{global_var}")

# 调用函数
print_hello()

# 参数和返回值
def add(a, b):
    return a + b

num =add(1,2)
print(num) # 3

# 多个返回值
def subtract(a, b):
    return a - b

num =subtract(1,2)
print(num) # -1

def multiply(a, b):
    return add(a,b), subtract(a,b)

num =multiply(1,2)
print(num) # (3, -1)
# 解包
n1,n2 = multiply(1,2)
print(n1) # 3
print(n2) # -1


def print_param(a,b,c,d):
    print(a,b,c,d)

# 传参方式1，位置参数
print_param(1,2,3,4)

# 传参方式2，关键字参数
print_param(a=1,b=2,c=3,d=4)

# 传参方式3，混合参数
print_param(1,2,c=3,d=4)

#默认参数
def print_position(country="中国",province="广东省",city="深圳"):
    print(f"country:{country},province:{province},city:{city}")

print_position()
print_position(country="美国")
print_position(country="美国",province="加利福利亚洲")
print_position(country="美国",province="加利福利亚洲",city="洛杉矶")

# 可变参数
def print_all(*args):
    for arg in args:
        print(arg)
print_all(1,2,3,4,5)

# 关键字参数
def print_all(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_all(a=1,b=2,c=3,d=4,e=5)

# 可变参数和关键字参数
def print_all_kw(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_all_kw(1,2,3,4,5,a=1,b=2,c=3,d=4,e=5)

# 匿名函数
print_name = lambda name: print(name)
print_name("nonaldo")
print_ling = lambda : print("-----------------")
print_ling()
multiply = lambda a,b: a*b
print(multiply(1,2)) # 2    

data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)
data_list.sort(key=lambda item : len(item)) # 匿名函数典型的应用场景 . 按字符串长度排序
print(data_list)

# 函数作为参数传入函数
def multiply_print(a,b,multiply_func):
    print(multiply_func(a,b))
multiply_print(1,2,multiply)
