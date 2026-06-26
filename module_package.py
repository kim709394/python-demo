""" 模块和包管理 
模块：.py文件
一个py文件为一个模块
"""

# 导入系统标准库的模块
import math # 直接导入math模块
from sys import path # 导入sys模块的path属性
import random as rd # 导入random模块，重命名为rd

# 导入自定义模块
from module.my_module import *
from module.my_module import print_separator3 as p3
# 导入自定义包
from pkg import *
from pkg.my_pkg2 import print_no21_30

# 调用模块的属性或者函数
print(math.pi) # 3.141592653589793
print(path) # ['C:\\Users\\bejamin\\python\\workspaces\\python-demo']
print(rd.randint(1,10)) # 1-10之间的随机整数

# 调用自定义模块的属性或者函数
print(PI)
print_separator1()
print_separator2()
p3()

# 调用自定义包的属性或者函数
my_pkg.print_no1_10()
my_pkg.print_no11_20()
print_no21_30()



