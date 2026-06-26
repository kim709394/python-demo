""" 流程控制 """
# if条件判断
num = 10
if num > 5:
    print("num大于5")

# if else
if num > 5:
    print("num大于5")
else:
    print("num小于5")

# if elif else
if num > 5:
    print("num大于5")
elif num < 5:
    print("num小于5")
else:
    print("num等于5")

""" 
    match条件匹配，类似java的switch语句
    匹配的值不局限于字符串，还可以是数字，每一个case不需要写break退出
    _ 表示匹配任意值，一般用于默认情况
"""
match num:
    case 10:
        print("num等于10")
    case 5:
        print("num等于5")
    case _:
        print("num等于其他值")
