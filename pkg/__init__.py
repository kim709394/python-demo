""" 包的初始化文件
    可以写一些描述性信息，比如包的版本号、作者、邮箱等
 """
__version__ = "1.0.0"
__author__ = "bejamin"
__email__ = "bejamin@example.com"
""" 
其他模块使用from pkg import *时，
只会导入__all__列表中的属性或者函数，其他属性或者函数不会被导入。
如果没有设置，那么将会导入所有属性或者函数。
 """
__all__ = ["my_pkg"] 
