""" 元组  tuple
元组是一种不可变的序列，用于存储多个值。
元组的元素可以是任意类型，也可以是不同的类型。
元组的元素是可重复，有序的，可以通过索引来访问。
"""
# 定义一个元组
t1 = (1,2,3,4,5)
print(t1)
# 元组的数据类型
print(type(t1)) # <class 'tuple'>

# 定义空元组
t2 = ()
print(t2)

# 定义只有一个元素的元组,需要在元素后面添加逗号
t3 = (100,)
print(t3)
print(type(t3)) # <class 'tuple'>

# 通过下标获取元素
print(t1[0]) # 1
print(t1[-1]) # 5

#切片
print(t1[1:3]) # (2, 3)

# count() 方法：统计元组中指定元素出现的次数
print(t1.count(2)) # 1

# len() 方法：返回元组的长度
print(len(t1)) # 5

# index() 方法：返回指定元素第一次出现的索引
print(t1.index(2)) # 1

# 遍历
for i in t1:
    print(i)

# 解包和组包
# 组包
t4 = (1,2,3,4,5)
print(t4)
t5 =1,2,3,4,5
print(t5)

# 基础解包，变量和元组的个数要一致
a,b,c,d,e = t4
print(a,b,c,d,e,sep="-")

# 扩展解包,将剩余元素收集到list集合中
first,second,*other,last = t4
print(first)     # 1
print(second)    # 2
print(other)    # [3, 4]
print(last)      # 5

*other,last1,last2 = t4
print(other)    # [1, 2, 3]
print(last1)    # 4
print(last2)    # 5

i,j,k = "a","b","c"
print(i,j,k)
i,j,k = k,i,j
print(i,j,k)


