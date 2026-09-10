# ============================================
# 学生成绩管理系统（修正版）
# 修正内容：
#   1. 功能3/4：用新输入变量 student / name1，不用残留的 name
#   2. 功能5：字典删除用 del，不用列表的 remove
#   3. 遍历：for name, score in items()（键=姓名，值=成绩）
#   4. 添加/修改：成绩用 int() 转换，不再存字符串
#   5. 功能6：用 values() + 累加套路 + 擂台套路重写
# ============================================

contacts = {}   # 姓名 → 成绩

while True:
    print("\n1.添加学生 2.查看所有 3.查找学生 4.修改成绩 5.删除学生 6.统计成绩 7.退出")
    if len(contacts) == 0:
        print("当前系统为空，请添加学生")
    else:
        print("当前学生成绩：")
        for name, score in contacts.items():      # 修正：键=姓名，值=成绩
            print(f"{name}: {score} 分")

    choice = input("请输入你的选择：")

    # ---- 功能 1：添加 ✅ ----
    if choice == "1":
        name = input("请输入学生姓名：")
        if name in contacts:
            print("该学生已存在，可用功能4修改")
        else:
            score = int(input("请输入学生成绩："))    # 修正：int 转换
            contacts[name] = score
            print(f"已添加{name}")

    # ---- 功能 2：查看所有 ✅ 修正变量顺序 ----
    elif choice == "2":
        for name, score in contacts.items():
            print(f"{name}的成绩是：{score}")

    # ---- 功能 3：查找 ✅ 修正：用 student ----
    elif choice == "3":
        student = input("请输入你要查找的学生姓名：")
        if student in contacts:
            print(f"{student}的成绩是：{contacts[student]}")
        else:
            print("系统中没有该学生")

    # ---- 功能 4：修改 ✅ 修正：用 name1 ----
    elif choice == "4":
        name1 = input("请输入你要修改的学生：")
        if name1 in contacts:
            new_score = int(input("请输入修改后的成绩："))
            contacts[name1] = new_score
            print(f"{name1}的成绩已修改为{new_score}")
        else:
            print("系统中没有该学生！")

    # ---- 功能 5：删除 ✅ 修正：del ----
    elif choice == "5":
        remove_name = input("请输入你要删除的学生：")
        if remove_name in contacts:
            del contacts[remove_name]
            print(f"{remove_name}已删除")
        else:
            print("系统中没有该学生")

    # ---- 功能 6：统计 ✅ 重写 ----
    elif choice == "6":
        if len(contacts) == 0:
            print("系统为空，无法统计")
        else:
            scores = list(contacts.values())   # 取出所有成绩当列表
            total = 0                          # 累加套路：平均分
            for s in scores:
                total = total + s
            average = total / len(scores)

            highest = scores[0]                # 擂台套路：最高最低
            lowest = scores[0]
            for s in scores:
                if s > highest:
                    highest = s
                if s < lowest:
                    lowest = s

            print(f"平均分：{average}")
            print(f"最高分：{highest}")
            print(f"最低分：{lowest}")

    # ---- 功能 7：退出 ✅ ----
    elif choice == "7" or choice == "q":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")
