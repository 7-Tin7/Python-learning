import random
import os
import datetime
class Friends:
    def __init__(self,name):
        self.name = name
        self.Affection = 10
        self.happiness = 30
        self.hunger = 20
    def feed1(self):
        self.hunger = self.hunger + 20
        self.happiness = self.happiness + 10
        self.Affection = self.Affection + 10
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{time_str}你带{self.name}出去吃了一顿，{self.name}特别开心，因为今天的饭菜很好吃")
        if self.hunger > 100:
            self.hunger = 100
            print(f"{self.name}已经吃饱了")
        if self.happiness > 100:
            self.happiness = 100
            print(f"{self.name}玩的特别开心,但是有点累了")
        if self.Affection > 100:
            self.Affection = 100
            print(f"{self.name}特别喜欢你！")
        elif self.Affection > 70:
            print(f"{self.name}对你有好感")
        else:
            print(f"{self.name}对你没有感觉")
    def feed2(self):
        self.hunger = self.hunger + 20
        self.happiness = self.happiness - 10
        self.Affection = self.Affection - 10
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{time_str}你带{self.name}出去吃了一顿，{self.name}不开心，因为今天{self.name}不想干这件事情")
        if self.hunger > 100:
            self.hunger = 100
            print(f"{self.name}已经吃饱了")
        if self.happiness < 0:
            self.happiness = 0
            print(f"{self.name}今天不开心呢，因为你的想法跟{self.name}想法没有走到一起")
        if self.Affection < 0:
            self.Affection = 0
            print(f"{self.name}很讨厌你！")
        elif self.Affection < 70:
            print(f"{self.name}对你有点生气")
        else:
            print(f"{self.name}对你没有感觉")
    def play1(self):
        self.hunger = self.hunger - 20
        self.happiness = self.happiness + 20
        self.Affection = self.Affection + 10
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{time_str} {self.name}牵着你的手，在公园逛了一圈，一起看到公园的花花草草，湖水飞鸟，{self.name}盯着你的眼睛，笑意盈盈地看着你^_^")
        if self.hunger < 0:
            self.hunger = 0
            print(f"{self.name}快饿死了")
        if self.happiness > 100:
            self.happiness = 100
            print(f"{self.name}玩的特别开心,但是有点累了")
            if self.Affection > 100:
                self.Affection = 100
                print(f"{self.name}特别喜欢你！")
            elif self.Affection > 70:
                print(f"{self.name}对你有好感")
            else:
                print(f"{self.name}对你没有感觉")
    def play2(self):
        self.hunger = self.hunger - 20
        self.happiness = self.happiness - 20
        self.Affection = self.Affection - 10
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{time_str}你牵着{self.name}的手，在公园逛了一圈，一起看到公园的花花草草，湖水飞鸟，可是你没注意到，{self.name}盯着你的眼睛，有点生气！")
        if self.hunger < 0:
            self.hunger = 0
            print(f"{self.name}快饿死了")
        if self.happiness < 0:
            self.happiness = 0
            print(f"{self.name}玩的特别不开心,而且对你不满")
            if self.Affection < 0:
                self.Affection = 0
                print(f"{self.name}非常讨厌你！")
            elif self.Affection < 70:
                print(f"{self.name}对你有一些不满")
            else:
                print(f"{self.name}对你没有感觉")
    def show(self):
        print(f"当前{self.name}饥饿感：{self.hunger},{self.name}的快乐值:{self.happiness},{self.name}对你的好感度:{self.Affection}")
    def send(self):
        goods = ["非洲之心","戒指","项链","手镯","耳环"]
        Affection1 = {"非洲之心":30,"戒指":20,"项链":10,"手镯":10,"耳环":10}
        choice = input("你要送什么东西给我呀？")
        if choice in goods:
            self.Affection = self.Affection + Affection1[choice]
            now = datetime.datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{time_str} {self.name}收到你的礼物咯，我好开心呀，谢谢你，真想亲亲你。。。")
            if self.Affection > 100:
                self.Affection = 100
                print(f"{self.name}特别喜欢你！")
            elif self.Affection > 70:
                print(f"{self.name}对你有好感")
            else:
                print(f"{self.name}对你没有感觉")
        else:
            print("好像没有这个东西呢")
Friends_name= input("给你的好友起个名字吧")
friends = Friends(Friends_name)
while True:
    print("1.出去吃大餐！ 2.一起出去玩玩呀！ 3.送礼物! 4.下次再见 5.查看当前状态")
    choice = input("你想要干什么呢？")
    computer = random.choice(["1","2"])
    if choice == "1" and computer == choice:
        friends.feed1()
    elif choice == "1" and computer != choice:
        friends.feed2()
    elif choice == "2" and computer == choice:
        friends.play1()
    elif choice == "2" and computer !=choice:
        friends.play2()
    elif choice == "3":
        friends.send()
    elif choice == "4":
        print("再见咯，我会一直在这里等你的 ^_^")
        break
    elif choice == "5":
        friends.show()
    else:
        print("你还想干什么坏事！做出正确的选项噢，我会一直陪着你的！")







