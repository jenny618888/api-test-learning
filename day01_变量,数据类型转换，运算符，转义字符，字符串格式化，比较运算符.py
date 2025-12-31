#2.1 变量
money = 50
print ("the wallet still left", money, "dollars")
icecream = 10
coke = 5
money = money - icecream
money = money - coke
print ("the wallet still left", money, "dollars")

#2.2数据类型
String_type = type ("apple")
int_type = type (666)
float_type = type (11.33)
print(String_type)
print(int_type)
print(float_type)

name = "apple"
type_name = type(name)
print(type_name)

#2.3数据类型转换
#整数11转换为字符串类型
string_name = str(11)
print (type(string_name), string_name)

#将字符串转换为数字
number = int("11")
print(type(number), number)

number2 = float("11.11")
print(type(number2), number2)

#整数转浮点数
float_num = float(13)
print(type(float_num), float_num)

#浮点数转整数
int_num = int(13.93)
print(type(int_num), int_num)

#2.7运算符
print("1+1=", 1+1)
print("1-1=", 1-1)
print("1*1=", 1*1)
print("1/1=", 1/1)
print("11//2=", 11//2)
print("11%2=", 11%2)
print("2**2=", 2**2)

num = 2
num += 1
print("num += 1:", num)

#2.8转义字符
name = '"apple"'
print(name)

name = "'banana"
print(name)

name = '\'orange'
print(name)
print(type(name))

#2.10字符串格式转化
name = "apple"
message = " I want eat an %s" % name
print(message)
print(type(name))
print(type(message))

#数字类型占位
class_num = 100
avg_salary = 20
message = "summary is %s, avarage salary is %s" % (class_num, avg_salary)
print(message)

#2.11 比较运算符
num1 = 10
num2 = 20
print(f"10 != 20's result is {num1 != num2}")
print(f"10 == 20's result is {num1 == num2}")
print(f"10 > 20's result is {num1 > num2}")