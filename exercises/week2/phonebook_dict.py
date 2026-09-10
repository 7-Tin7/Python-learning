# ============================================
# 手机通讯录（字典版 · 方案 B）📒
#
# 核心设计：contacts = {号码: 姓名}
#   - 被查找的东西（号码）做键，要显示的东西（姓名）做值
#   - 查找：contacts[号码] 一步到位
#   - 键不能重复 → 自动防止一个号码对应两个人
# ============================================

contacts = {}   # 空字典：号码 → 姓名

while True:
    # ---- 第一件事：显示当前状态 ----
    if len(contacts) == 0:
        print("当前通讯录为空，请添加联系人")
    else:
        print("当前通讯录：")
        for number, name in contacts.items():
            print(f"{name}: {number}")

    # ---- 第二件事：菜单（永远显示）----
    print("1.添加联系人 2.查找电话 3.退出")
    choice = input("请输入选择:")

    if choice == "1":
        new_person = input("请输入要添加的联系人姓名:")
        new_number = input(f"请输入{new_person}的电话:")
        contacts[new_number] = new_person          # 号码做键，姓名做值
        print(f"已添加：{new_person}")

    elif choice == "2":
        number = input("请输入你要查找的电话:")
        if number in contacts:                     # 判断键在不在
            print(f"该电话联系人是{contacts[number]}")   # 直接取值
        else:
            print("该号码不存在通讯录中")

    elif choice == "3":
        print("退出通讯录，再见！")
        break
    else:
        print("无效的选择，请重新输入")
