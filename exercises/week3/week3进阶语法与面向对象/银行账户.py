class account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    def deposit(self):
        try:
            num = float(input("请输入你要存入的金额："))
        except ValueError:
            print("请输入数字")
            return
        self.balance = self.balance + num
        print(f"已存入{num}元，账户余额：{self.balance}元")
    def withdraw(self):
        try:
            num1 = float(input("请输入你要取出的金额："))
        except ValueError:
            print("请输入数字")
            return
        if num1 > self.balance:
            print("余额不足")
        else:
            self.balance = self.balance - num1
            print(f"已取出{num1}元，账户余额：{self.balance}元")
    def show(self):
        print(f"当前余额：{self.balance}")
Owner = input("请输入户主姓名")
my_account = account(Owner)
while True:
    print("1.存钱 2.取钱 3.查看余额 4.退出")
    choice = input("请输入你的选择：")
    if choice == "1":
        my_account.deposit()
    elif choice == "2":
        my_account.withdraw()
    elif choice == "3":
        my_account.show()
    elif choice == "4":
        print("再见！")
        break
    else:
        print("无效的选择")
