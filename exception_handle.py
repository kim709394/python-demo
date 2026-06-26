""" 异常处理，类似java的try-catch 
    异常会逐层往上传递
"""
try:
    print(hello)
except NameError as e:  # 捕捉类型未定义异常
    print("hello变量未定义,异常信息：",e)

try:
    10/0
except ZeroDivisionError as e:  # 捕捉除数为0的异常
    print("除数为0,异常信息：",e)

try:
    l1 = [1,2,3,4,5]
    print(l1[5])
except IndexError as e:  # 捕捉索引超出范围的异常
    print("索引超出范围,异常信息：",e)

try:
    raise Exception("这是一个异常") # 手动抛出异常
except Exception as e:  # 捕捉所有异常
    print("这是一个异常,异常信息：",e)
    
def test1():
    test2()

def test2():
    test3()

def test3():
    raise Exception("这是一个异常")

test1()