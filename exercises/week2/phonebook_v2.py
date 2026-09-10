# ============================================
# 手机通讯录（修正版）📒
#
# 修正内容：
#   1. 空判断：len(person) == 0（不是 len((person, numbers)) == "0"）
#   2. 查找电话：遍历 person 找匹配，而不是用上次遗留的 new_person
#   3. 结构：状态显示和菜单分开，菜单永远显示
#   4. 联系人列表自动显示，"查看所有"菜单项就省掉了
# ============================================

person = []          # 存 (姓名, 电话) 元组的列表
numbers = set()      # 存电话号码（去重用）

while True:
    # ---- 第一件事：显示当前状态 ----
    if len(person) == 0:
        print("当前通讯录为空，请添加联系人")
    else:
        print("当前通讯录：")
        for name, num in person:
            print(f"{name}: {num}")

    # ---- 第二件事：菜单（永远显示）----
    print("1.添加联系人 2.查找电话 3.退出")
    choice = input("请输入选择:")

    if choice == "1":
        new_person = input("请输入要添加的联系人姓名:")
        new_number = input(f"请输入{new_person}的电话:")
        person.append((new_person, new_number))
        numbers.add(new_number)

    elif choice == "2":
        number = input("请输入你要查找的电话:")
        found = False                        # 旗帜变量：默认没找到
        for name, num in person:             # 遍历找匹配
            if num == number:
                print(f"该电话联系人是{name}")
                found = True
                break
        if not found:
            print("该号码不存在通讯录中")

    elif choice == "3":
        print("退出通讯录，再见！")
        break
    else:
        print("无效的选择，请重新输入")
