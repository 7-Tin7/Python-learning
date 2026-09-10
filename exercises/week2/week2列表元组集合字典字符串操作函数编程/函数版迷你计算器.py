def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
while True:
    print("1.加法 2.减法 3.乘法 4.除法")
    choice = input("请选择")
    if choice == "1":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相加和为：{add(a,b)}")
    elif choice == "2":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相减的差为：{subtract(a,b)}")
    elif choice == "3":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相乘的积为：{multiply(a,b)}")
    elif choice == "4":
        a = float(input("请输入第一个数："))
        b = float(input("请输入第二个数："))
        print(f"两数相除的商为：{divide(a,b)}")
    else:
        print("无效的选择，请重新输入！")
