# ============================================
# 仓库管理系统 v2（字典版 · 改进版）
#
# 改进点：
#   1. price 和 cash_price 合并成一个 price 字典
#   2. 出售时 property 相应减少（避免"凭空造钱"）
#   3. 显示仓库时去掉多余的 in 检查（添加时已验证）
# ============================================

storage = []
property = 0          # 仓库资产（物品价值）
cash = 0              # 现金
price = {"非洲之心": 1000, "海洋之泪": 2000, "特里克头盔": 100, "特里克护甲": 200}
game_goods = list(price.keys())   # 从字典直接取出所有物品名！

while True:
    print(f"游戏货物有: {', '.join(game_goods)}")
    if len(storage) == 0:
        print("当前仓库里没有任何东西，请添加")
    else:
        print("当前仓库资产：")
        for i, goods in enumerate(storage):
            print(f"{i + 1}.{goods}")

    print("1.添加物品到仓库 2.出售物品 3.退出仓库")
    choice = input("请输入选择")

    if choice == "1":
        new_goods = input("请输入要添加的物资：")
        if new_goods in game_goods:
            storage.append(new_goods)
            property = property + price[new_goods]
            print(f"{new_goods}已添加到仓库")
        else:
            print("游戏中不存在该物资")
        print(f"您的总资产为{property}")
        print(f"您的现金为{cash}")

    elif choice == "2":
        remove_goods = input("请输入要出售的物资：")
        if remove_goods in storage:
            storage.remove(remove_goods)
            cash = cash + price[remove_goods]        # 现金增加
            property = property - price[remove_goods] # 资产减少
            print(f"{remove_goods}已出售")
            print(f"您的总资产为{property}")
            print(f"您的现金为{cash}")
        else:
            print(f"您的仓库中没有{remove_goods}")

    elif choice == "3" or choice == "q":
        print("已退出您的仓库，再见！")
        break
    else:
        print("没有这个选项，请重新输入")
