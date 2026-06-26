""" 循环控制语句 """
# while循环

num = 0
while num < 10:
    print(f"num等于{num}")
    num += 1
print("循环结束")

# for循环,range()范围函数,默认从0开始包前不包后，i=0~9
for i in range(10):
    print(f"i等于{i}")
print("循环结束")

# i=1~9
for i in range(1,10):
    print(f"i等于{i}")
print("循环结束")

# 设置范围的步长为2，i=1 3 5 7 9
for i in range(1,10,2):
    print(f"i等于{i}")
print("循环结束")

# 给定字符串，循环获得每一个字符
str = "hello"
for char in str:
    print(f"char等于{char}")
print("循环结束")

# 嵌套循环,输出99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")    #指定结束符为制表符
    print()
