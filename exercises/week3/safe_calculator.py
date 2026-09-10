# ============================================
# 第 3 周 练习：防崩溃计算器 🛡️
#
# 功能：和之前计算器一样，但这次——
#   1. 输入 abc 不崩溃（try/except 接住 ValueError）
#   2. 除以 0 不崩溃（try/except 接住 ZeroDivisionError）
#
# 新知识：try / except
# 旧知识：函数 def / return / while / if-elif / float
# ============================================

# ---- TODO 1：安全输入函数 ----
# 写一个 get_number(prompt) 函数，永远返回合法数字：
#   def get_number(prompt):
#       while True:
#           try:
#               return float(input(prompt))   # 成功 → 返回数字
#           except ValueError:                 # 输入 abc 会走到这里
#               print("输入的不是数字，请重新输入！")
#
# 测试：x = get_number("请输入第一个数：") 后，
#       无论用户输入什么，x 一定是合法数字（绝不崩溃）

# ---- TODO 2：主程序（除法已帮你写好异常处理）----
while True:
    print("1.加法 2.减法 3.乘法 4.除法 5.退出")
    choice = input("请选择：")

    if choice == "5" or choice == "q":
        print("再见！")
        break

    x = get_number("请输入第一个数：")     # 不崩溃
    y = get_number("请输入第二个数：")     # 不崩溃

    if choice == "1":
        print(f"结果：{x + y}")
    elif choice == "2":
        print(f"结果：{x - y}")
    elif choice == "3":
        print(f"结果：{x * y}")
    elif choice == "4":
        # 除法可能除以 0 → 用 try/except 接住
        try:
            print(f"结果：{x / y}")
        except ZeroDivisionError:
            print("除数不能为 0！")
    else:
        print("无效的选择，请重新输入")

# 测试用例：
#   加法：输入 10 和 3 → 13.0
#   除法：输入 10 和 0 → "除数不能为 0！"（不崩溃！）
#   任意操作：输入 abc → "输入的不是数字，请重新输入！"（不崩溃！）
# ============================================
