class Pet:
    def __init__(self,name):
        self.name = name
        self.hunger = 20
        self.happiness = 20
    def feed(self):
        self.hunger = self.hunger - 20
        self.happiness = self.happiness + 10
        if self.hunger < 0:
            self.hunger = 0
        if self.happiness > 100:
            self.happiness = 100
        print(f"你喂了{self.name},它很开心")
    def play(self):
        self.happiness = self.happiness + 30
        self.hunger = self.hunger + 10
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger > 100:
            self.hunger = 100
        print(f"你陪{self.name}完了一会，{self.name}很开心")
    def show(self):
        print(f"{self.name}的状态：饥饿值：{self.hunger} 快乐值：{self.happiness}")
        if self.happiness >= 90:
            print(f"{self.name}超级开心")
        elif self.happiness <= 30:
            print(f"{self.name}超级难受")
pet_name = input("给你的宠物起个名：")
pet = Pet(pet_name)
while True:
    print("1.喂食 2.陪玩 3.查看状态 4.退出")
    choice = input("请输入你的选择：")
    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.show()
    elif choice == "4":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")

