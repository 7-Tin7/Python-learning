# ============================================
# 第 2 周 练习：函数版迷你计算器（修正版）🧮
#
# 修正内容：
#   1. 函数用 return 交货，不在函数里 print
#   2. 调用函数加括号并传参：add(a, b)
#   3. 输入用 float() 转数字（否则字符串拼接 "10"+"3"="103"）
#   4. 修正错别字：tow → b，devide → divide
# ============================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("1.加法 2.减法 3.乘法 4.除法 5.退出")
    choice = input("请选择：")

    if choice == "5" or choice == "q":
        print("再见！")
        break

    if choice == "1":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相加的和为：{add(a, b)}")
    elif choice == "2":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相减的差为：{subtract(a, b)}")
    elif choice == "3":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相乘的积为：{multiply(a, b)}")
    elif choice == "4":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相除的商为：{divide(a, b)}")
