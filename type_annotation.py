""" 类型注解,类似typescript的语法，给弱类型变量加上强制类型注解 """
num: int = 10
num1: float = 10.5
s: str = "nonaldo"
boo: bool = True
null: None = None

l1: list[str | int] = ["a",1,"b",2] # 列表中可以包含字符串和整数
set1: set[str | int] = {"a",1,"b",2} # 集合中可以包含字符串和整数
d1: dict[str | any] = {"a":1,"b":2} # 字典中键值对的键是字符串，值可以是任意类型
t1: tuple[str | int] = ("a",1,"b",2) # 元组中可以包含字符串和整数

# 函数类型注解
def add(a: int, b: int) -> int:
    return a + b

result = add(1,2)
print(result) # 3
def print_list(t1: tuple[str | int]) -> str:
    print(t1,sep=",")
    return t1.__str__()
print_list(("a",1,"b",2))
