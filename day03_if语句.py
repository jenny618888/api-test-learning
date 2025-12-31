#input() get information from the keyboard
print("tell me who are you")
name = input()
print("I see, you are: %s" % name)

name = input("tell me who are you")
print("I see, you are: %s" % name)

age = 30
if age >= 18:
    print(" I am an adult")
    print(" I am going to the college")
print("time is fast")

print("Welcome to the park")
age = input("please enter your age")
if int(age) > 18:
    print("please afford more 10 dollars")
print("Hope you have fun")

age = int(input("please enter your age"))
if age >= 18:
    print("please afford more 12 dollars")
else: #不需要判断条件
    print("Having fun")


if int(input("please enter your height")) < 120:
    print("height less than 120, for free")
elif int(input("please enter your vip level")) > 3:
    print("vip level greater than 3, for free")
elif int(input("please tell me what day is it")) == 1:
    print("today is 1st, for free")
else:
    print("you need to buy the ticket")

num = 128
if int(input("enter the first number you guess")) == num:
    print("you are right")
elif int(input("no, please enter another number")) == num:
    print("you are right")
elif int(input("no, please guess the number in the last")) == num:
    print("yes, you are right")
else:
    print("sorry, you failed, the right number is 128")

