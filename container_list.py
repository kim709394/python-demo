""" 
    list集合
 """
# 定义一个列表,不限制元素数据类型
list1 = [1,2,3,4,5,6,7,8,9,"hello","list",True]
print(list1)
print(type(list1)) # 列表的数据类型：<class 'list'>

# 访问元素
print(list1[0]) # 1 列表下标从0开始
print(list1[-1]) # True 反向访问元素，列表反向下标从-1开始，-1表示最后一个元素

# 修改元素
list1[0] = 100
print(list1)

# 删除元素
del list1[0]
print(list1)

# 清空列表
list1.clear()
print(list1)

# 清空列表并且删除整个列表
del list1
# print(list1)    # 报错，列表已被删除

# 遍历
l2 = [1,2,3,4,5,6,7,8,9,'nonado',False]
for item in l2:
    print(item,end="\t")

# 列表切片,从列表中切出下标范围的元素，生成一个新的列表，下标包前不包后
print(l2[0:5]) # [1, 2, 3, 4, 5]
print(l2[5:]) # [6, 7, 8, 9, 'nonado', False]   从[5]开始切片，直到列表结束
print(l2[0:5:2]) # [1, 3, 5]   从[0]开始切片，步长为2，每2个元素取一个,l2[0],l2[2],l2[4]
print(l2[0:-2:1])    # [1, 2, 3, 4, 5, 6, 7, 8, 9]   从[0]开始切片，步长为1，每1个元素取一个,l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6],l2[7]

""" 列表的常用方法 """
#定义列表
l3 = ["a","b","c","d","e","f","g","h","i","j"]
print(l3)

# 往末位追加元素
l3.append("k")
print(l3)

# 在指定索引之前插入元素
l3.insert(10,"l")
print(l3)

# 移除第一个匹配到的元素
l3.remove("l")
print(l3)

# 删除指定索引位置的元素并返回，如果未指定则默认删除最后一个
ele =l3.pop(1)
print(ele)
print(l3)
print(l3.pop())
print(l3)

# 从小到大排序
l4 = [1,3,2,4,5,7,6,8,9,10]
l4.sort()
print(l4)

# 翻转元素
l4.reverse()
print(l4)   

# 合并两个列表
l5 = [11,12,13]
l6 = [*l4,*l5]
# l6 = l4 + l5
print(l6)

# 判断列表是否包含指定元素
print("a" in l6) # False
print(6 in l6) # True
print(14  not in l6) # True

# 对列表每个元素按照规则生成一个新的列表，例如：对列表每个元素取平方
l7 = [item**2 for item in l6]
print(l7)

# 筛选符合规则的列表元素，然后再按新规则生成一个新列表,例如：筛选出偶数，再对偶数取平方
l8 = [item**2 for item in l6 if item%2==0]
print(l8)
