#字符串字面量之间的拼接
print("apple" + " is good")

#字符串字面量和字符串变量之间的拼接,error!
name = "jenny"
address = "park"
tel = "12345"
print ("My name is:" + name + ", My address is:" + address + ", My tel is" + tel)

#字符串格式化的精度控制
num1 = 11
num2 = 11.345
print ("数字11宽度限制5，结果是：%5d" % num1)
print ("数字11宽度限制1，结果是：%1d" % num1)
print ("数字11.345宽度限制7，结果是：%7.2f" % num2)
print ("数字11.345宽度不限制，结果是：%.2f" % num2)

#字符串格式化方式2
name = "apple"
set_up_year = 2006
stock_price = 19.99
print(f"The company is {name}, which set up in {set_up_year}, and the stock price is {stock_price}")

#对表达式进行字符串格式化
print("1*1的结果是：%d" % (1 * 1))
print(f"1*2的结果是：{1 * 2}" )
print("字符串在python中的类型名是：%s" % type("字符串"))

#练习
name = "Apple"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"The company is {name}; the stock code is {stock_code}; the stock price is {stock_price}; ",
      "the daily growth factor is %f, after %d, the stock price goes to %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price*stock_price_daily_growth_factor**growth_days))

