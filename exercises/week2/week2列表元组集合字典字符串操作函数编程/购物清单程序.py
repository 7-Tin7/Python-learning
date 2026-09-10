"""shopping_list = []
while True:
    if len(shopping_list) == 0:
        print("当前清单列表为空")
    else:
        print("当前清单：")
        for i,item in enumerate(shopping_list):
            print(f"{i+1}.{item}")  #显示编号
    print("1.添加物品 2.删除物品 3.退出")
    choice = input("请选择:")
    if choice == "1":
        new_item = input("请输入要添加的物品:")
        shopping_list.append(new_item)
        print(f"已添加{new_item}")
    elif choice == "2":
        remove_item = input("请输入要删除的物品：")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"已删除{remove_item}")
        else:
            print(f"清单里没有这件物品")
    elif choice == "3" or choice == "q":
        print(f"再见！")
        break
    else:
        print("无效的选择，请重新输入！")"""






"""shopping_list = []
while True:
    if len(shopping_list) == 0:
        print("当前清单是空的")
    else:
        print("当前清单：")
        for i,item in enumerate(shopping_list):
            print(f"{i+1}.{item}")
    print("1.添加物品 2.删除物品 3.退出")
    choice = input("请输入")
    if choice == "1":
        new_item = input("请输入要添加的物品：")
        shopping_list.append(new_item)
        print(f"{new_item}已添加到清单")
    elif choice == "2":
        remove_item = input("请输入要删除的物品：")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"{remove_item}已从清单中删除")
        else:
            print("当前清单中没有该物品")
    elif choice == "3" or choice == "q":
        print(f"再见！")
        break
    else:
        print("无效的选择，请重新输入")"""






shopping_list = []
while True:
    if len(shopping_list) == 0:
        print("当前清单为空")
    else:
        print("当前清单：")
        for i, item in enumerate(shopping_list):
            print(f"{i+1}.{item}")
    print("1.添加物品 2.删除物品 3.退出")
    choice = input("请输入选择")
    if choice == "1":
        new_item = input("请输入要添加的物品：")
        shopping_list.append(new_item)
        print(f"{new_item}已添加到清单")
    elif choice == "2":
        remove_item = input("请输入要删除的物品:")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"{remove_item}已从清单中删除")
        else:
            print(f"当前清单中没有该物品")
    elif choice == "3" or choice == "q":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入！")













