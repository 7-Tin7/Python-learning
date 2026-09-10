def add(a,b):
    return a + b
def divide(a,b):
    return a / b
while True:
    print("1.加法 2.除法 3.退出")
    num = input("请输入选择：")
    if num == "1":
        try:
            a = float(input("请输入第一个数字"))
            b = float(input("请输入第二个数字"))
            print(f"两数相加和为：{add(a,b)}")
        except ValueError:
            print("输入的不是数字,请重新输入")
    elif num == "2":
        try:
            a = float(input("请输入第一个数字"))
            b = float(input("请输入第二个数字"))
            print(f"两数相除商为：{divide(a,b)}")
        except ValueError:
            print("输入的不是数字，请重新输入")
        except ZeroDivisionError:
            print("除数不能为0，请重新输入")
    elif num =="3":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")
