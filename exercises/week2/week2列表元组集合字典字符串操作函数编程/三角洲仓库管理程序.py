"""storage = []
property = 0
heart = 1000
sea_tear = 2000
helmet = 100
armor = 200
cash = 0
game_goods = ["非洲之心","海洋之泪","特里克头盔","特里克护甲"]
while True:
    print(f"游戏货物有:{', '.join(game_goods)}")
    if len(storage) == 0:
        print("当前仓库里没有任何东西，请添加")
    else:
        print("当前仓库资产：")
        for i,goods in enumerate(storage):
            if goods in game_goods:
                print(f"{i + 1}.{goods}")
    print("1.添加物品到仓库 2.出售物品 3.退出仓库")
    choice = input("请输入选择")
    if choice == "1":
        new_goods = input("请输入要添加的物资：")
        if new_goods in game_goods:
            storage.append(new_goods)
            print(f"{new_goods}已添加到仓库")
            if new_goods == "非洲之心":
                property = property + heart
            elif new_goods == "海洋之泪":
                property = property + sea_tear
            elif new_goods == "特里克头盔":
                property = property + helmet
            elif new_goods == "特里克护甲":
                property = property + armor
        else:
            print("游戏中不存在该物资")
        print(f"您的总资产为{property}")
        print(f"您的现金为{cash}")
    elif choice == "2":
        remove_goods = input("请输入要出售的物资：")
        if remove_goods in storage:
            storage.remove(remove_goods)
            print(f"{remove_goods}已出售")
            if remove_goods == "非洲之心":
                cash = cash + heart
            elif remove_goods == "海洋之泪":
                cash = cash + sea_tear
            elif remove_goods == "特里克头盔":
                cash = cash + helmet
            elif remove_goods == "特里克护甲":
                cash = cash + armor
            print(f"您的总资产为{property}")
            print(f"您的现金为{cash}")
        else:
            print(f"您的仓库中没有{remove_goods}")
    elif choice == "3" or choice == "q":
        print("已退出您的仓库，再见！")
        break
    else:
        print("没有这个选项，请重新输入")"""



storage = []
property = 0
cash = 0
price = {"非洲之心":1000,"海洋之泪":2000,"特里克头盔":100,"特里克护甲":200}
game_goods = ["非洲之心","海洋之泪","特里克头盔","特里克护甲"]
while True:
    print(f"游戏货物有:{', '.join(game_goods)}")
    if len(storage) == 0:
        print("当前仓库里没有任何东西，请添加")
    else:
        print("当前仓库资产：")
        for i,goods in enumerate(storage):
            if goods in game_goods:
                print(f"{i + 1}.{goods}")
    print("1.添加物品到仓库 2.出售物品 3.退出仓库")
    choice = input("请输入选择")
    if choice == "1":
        new_goods = input("请输入要添加的物资：")
        if new_goods in game_goods:
            storage.append(new_goods)
            print(f"{new_goods}已添加到仓库")
            property = property + price[new_goods]
        else:
            print("游戏中不存在该物资")
        print(f"您的总资产为{property}")
        print(f"您的现金为{cash}")
    elif choice == "2":
        remove_goods = input("请输入要出售的物资：")
        if remove_goods in storage:
            storage.remove(remove_goods)
            print(f"{remove_goods}已出售")
            cash = cash + price[remove_goods]
            print(f"您的总资产为{property}")
            print(f"您的现金为{cash}")
        else:
            print(f"您的仓库中没有{remove_goods}")
    elif choice == "3" or choice == "q":
        print("已退出您的仓库，再见！")
        break
    else:
        print("没有这个选项，请重新输入")