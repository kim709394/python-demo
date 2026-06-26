import math
""" 

 __all__也是python的内置变量，意思是当其他模块使用from my_module import *时，
   只会导入__all__列表中的属性或者函数，其他属性或者函数不会被导入。
   如果没有设置，那么将会导入所有属性或者函数。
 """
__all__=["PI","print_separator1","print_separator2"]

PI = math.pi

def print_separator1():
    print("-" * 30)

def print_separator2():
    print("*" * 30)

def print_separator3():
    print("#" * 30)

"""     
__name__变量是python的内置变量，不需要预先定义，假如当前文件被执行，
__name__变量的值为"__main__"，否则为模块名。
 """
if __name__ == "__main__":
    print_separator1()

print(__name__)
   