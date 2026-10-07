# ============================================
# 第 2 周 练习 1：购物清单程序（参考答案）🛒
# ============================================

shopping_list = []  # 空列表，用来存物品

while True:

    # ---- TODO 1：显示当前清单 ----
    if len(shopping_list) == 0:
        print("🛒 清单是空的")
    else:
        print("🛒 当前清单：")
        for i, item in enumerate(shopping_list):
            print(f"{i + 1}. {item}")

    # ---- TODO 2：显示菜单 ----
    print("1. 添加物品  2. 删除物品  3. 退出")
    choice = input("请选择：")

    # ---- TODO 3：添加物品 ----
    if choice == "1":
        new_item = input("请输入要添加的物品：")
        shopping_list.append(new_item)          # 添加到末尾
        print(f"已添加：{new_item}")

    # ---- TODO 4：删除物品 ----
    elif choice == "2":
        remove_item = input("请输入要删除的物品：")
        if remove_item in shopping_list:        # 先确认在不在
            shopping_list.remove(remove_item)   # 在才删，否则会报错
            print(f"已删除：{remove_item}")
        else:
            print("清单里没有这件物品")

    # ---- TODO 5：退出 ----
    elif choice == "3" or choice == "q":
        print("再见！")
        break

    # 加一个小改进：输入了别的选项就提示重来
    else:
        print("无效的选择，请重新输入！")
