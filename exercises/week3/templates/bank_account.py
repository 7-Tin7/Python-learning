# ============================================
# 第 3 周 练习 2：银行账户 💰
# 和"虚拟宠物"同款结构，巩固 class 语法！
#
# 功能：开户 → 存款 / 取款 / 查看余额 / 退出
#
# 新知识：类 class / __init__ / self / 属性 / 方法
# 旧知识：while / if-elif / input / float / print
# ============================================

# ---- TODO 1：定义 BankAccount 类 ----
class BankAccount:
    def __init__(self, owner):       # 构造方法：开户时初始化
        self.owner = owner           # 属性：户主名字
        self.balance = 0.0           # 属性：余额，初始 0

    # ---- TODO 2：存款方法 ----
    # def deposit(self, amount):          # amount 是存多少钱
    #     self.balance = self.balance + amount    # 余额增加（累加套路！）
    #     print(f"存入 {amount} 元，当前余额 {self.balance} 元")

    # ---- TODO 3：取款方法（注意余额不足！）----
    # def withdraw(self, amount):
    #     if amount <= self.balance:          # 钱够才让取
    #         self.balance = self.balance - amount
    #         print(f"取出 {amount} 元，当前余额 {self.balance} 元")
    #     else:
    #         print("余额不足！")              # 钱不够拒绝

    # ---- TODO 4：查看余额方法 ----
    # def show(self):
    #     print(f"{self.owner} 的余额：{self.balance} 元")

# ---- TODO 5：主程序 ----
# 1. 开户：owner = input("请输入户主姓名：")
#          account = BankAccount(owner)     ← 创建对象！
# 2. while True 菜单：
#    print("1.存款 2.取款 3.查看余额 4.退出")
#    choice = input("请选择：")
#    if choice == "1":
#        amount = float(input("存入金额："))
#        account.deposit(amount)            ← 对象.方法(参数)
#    elif choice == "2":
#        amount = float(input("取出金额："))
#        account.withdraw(amount)
#    elif choice == "3":
#        account.show()
#    elif choice == "4" or choice == "q":
#        print("再见！"); break
#    else:
#        print("无效的选择")

# 测试：
#   开户"小明" → 存 1000 → 取 300 → 余额 700
#   取 9999 → 提示"余额不足！"（不崩溃）
# ============================================
