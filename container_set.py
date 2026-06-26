""" 
set集合
无序、唯一，可修改
 """

# 定义set
s1 = {1,2,3,4,5}
print(s1)
print(type(s1)) # <class 'set'>

# 定义空set
s2 = set()
print(s2)
print(type(s2)) # <class 'set'>

# 常用方法
# add() 方法：添加元素
s1.add(6)
print(s1)    # {1, 2, 3, 4, 5, 6}

# remove() 方法：删除元素
s1.remove(6)  
print(s1)    # {1, 2, 3, 4, 5}

# clear() 方法：清空集合
s1.clear()
print(s1)    # set()

# 遍历
s1 = {1,2,3,4,5}
for i in s1:
    print(i)

# pop() 方法：随机删除一个元素
s1.pop()
print(s1)    

# 求两个集合的差集
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
# difference() 方法：求两个集合的差集，即存在第一个集合中，不存在第二个集合中的元素
print(s1.difference(s2)) # {1, 2}
print(s1-s2) # {1, 2}
print(s2.difference(s1)) # {6, 7}
print(s2-s1) # {6, 7}

# union() 方法：求两个集合的并集，即包含两个集合中所有的元素
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7}
print(s1|s2) # {1, 2, 3, 4, 5, 6, 7}
print(s1 or s2) # {1, 2, 3, 4, 5, 6, 7}

# intersection() 方法：求两个集合的交集，即同时存在于两个集合中的元素
print(s1.intersection(s2)) # {3, 4, 5}
print(s1&s2) # {3, 4, 5}
print(s1 and s2) # {3, 4, 5}

# 获取集合的长度
print(s1.__len__()) # 5
print(len(s1)) # 5




