""" 面向对象，类的定义和使用 """
# 定义一个类，在创建类的时候动态添加属性，不推荐这种方式
class Student:
    pass

# 实例化类
s1 = Student()
# 给实例添加属性
s1.name = "张三"
s1.age = 18
s1.score = 90
print(s1)
print(s1.age)
print(s1.__dict__)  # 以字典的形式打印类的信息

#标准方法定义类.类名大写
class Student:

    # 类的属性，所有实例共享，类似于java的静态变量
    school = "清华大学"


    """ 初始化的方法，类似java的构造方法，
    实例化时调用这个方法
     用于初始化对象的属性
     self：第一个参数，表示当前对象实例
       """
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 魔法方法，打印对象实例时调用的方法，
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，成绩：{self.score}"
    # 魔法方法，比较对象实例时调用的方法，
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.score == other.score
    
    # 魔法方法，比较对象实例时调用的方法，
    def __lt__(self, other):
        return self.score < other.score
    
    #自定义类的方法,例如：考试方法
    def test(self,subject):
        print(f"{self.name}正在测试{subject}")
        return self.score
   
s2 = Student("李四",18,80)
s3 = Student("王五",19,90)
print(s2)
# 类属性直接用类名调用
print(s2.school)
# 测试魔法方法
print(s2 == s3)
print(s2 < s3)
# 测试自定义方法
print(s2.test("数学"))
print(s3.test("英语"))
