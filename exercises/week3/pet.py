# ============================================
# 第 3 周 练习：虚拟宠物（参考答案）🐱
# ============================================

class Pet:
    # 构造方法：创建宠物时自动执行，初始化属性
    def __init__(self, name):
        self.name = name           # 属性：名字
        self.hunger = 30           # 属性：饥饿值（初始 30）
        self.happiness = 70        # 属性：快乐值（初始 70）

    # 方法：喂食 —— 用 self.xxx 修改自己的属性
    def feed(self):
        self.hunger = self.hunger - 20       # 吃饱，饥饿下降
        self.happiness = self.happiness + 10  # 有吃的，快乐上升

        if self.hunger < 0:                  # 防护：饥饿不能变负数
            self.hunger = 0
        if self.happiness > 100:             # 防护：快乐封顶 100
            self.happiness = 100

        print(f"你喂了{self.name}，它很开心！")

    # 方法：玩耍
    def play(self):
        self.happiness = self.happiness + 20  # 陪玩，快乐上升
        self.hunger = self.hunger + 10        # 玩累了，变饿

        if self.happiness > 100:
            self.happiness = 100
        if self.hunger > 100:
            self.hunger = 100

        print(f"你陪{self.name}玩了一会儿！")

    # 方法：查看状态
    def show(self):
        print(f"{self.name}的状态：饥饿值 {self.hunger}，快乐值 {self.happiness}")
        if self.happiness >= 90:
            print(f"{self.name}超级开心！😄")
        elif self.happiness < 40:
            print(f"{self.name}心情不好……😢")


# ---- 主程序：创建对象 + 菜单循环 ----
pet_name = input("给你的宠物起个名字：")
pet = Pet(pet_name)              # ← 创建对象！自动调用 __init__

while True:
    print("1.喂食 2.陪玩 3.查看状态 4.退出")
    choice = input("请选择：")

    if choice == "1":
        pet.feed()               # ← 调用方法：对象.方法()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.show()
    elif choice == "4" or choice == "q":
        print("再见！")
        break
    else:
        print("无效的选择")
