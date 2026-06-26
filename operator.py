""" 运算符 """
# 算术运算符，如+, -, *, /, %, //, **等,加减乘除，取余数，整除，次方幂
num1 =10
num2 =5
num3 =4
print(num1+num2) # 15
print(num1-num2) # 5
print(num1*num2) # 50
print(num1/num3) # 2.5  
print(num1%num2) # 0
print(num1//num3) # 2
print(num1**num2) # 100000
# # 算术运算符的优先级 --> **  --> *  /  //  %   --> +  -
print("0.1 + 10 / 4**2 = ", 0.1 + 10 / 4 ** 2)
# 浮点数的运算丢失精度问题，计算机是二进制，无法完整显示浮点数
print("2.8-1.3 = ", 2.8-1.3) # 1.4999999999999998

# 赋值运算符: = += -= *= /= %= //= **=
num4 = 100
print(num4) # 100
num4 +=1
print(num4) # 101
num4 -=1
print(num4) # 100
num4 *=2
print(num4) # 200
num4 //=2
print(num4) # 100
num4 %=3
print(num4) # 1
num4 /=0.1
print(num4) # 10.00
num4 **=2
print(num4) # 100.0

# 比较运算符: ==  !=  >  >=  <  <= 
print(10 == 10) # True
print(10 != 10) # False
print(10 > 5) # True
print(10 >= 5) # True
print(10 < 5) # False
print(10 <= 5) # False

#逻辑运算符: and   or   not 
print(True and True) # True
print(True or False) # True
print(not True) # False
num5 = input("请输入一个数字：")
num5 = int(num5)

print(f"你输入的数字是：{num5},他是否在10到20之间：{10<=num5<=20}")
print(f"你输入的数字是：{num5},他是否在10到20之间：{num5>=10 and num5<=20}")




