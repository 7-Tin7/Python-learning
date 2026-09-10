# ============================================
# 学生成绩管理系统（最终修正版 v3）
#
# 本版修正：功能 1 / 4 的输入验证
#   正确顺序：字符串 → isdigit 检查 → int 转换 → 范围检查 → 存储
#   （原来先 int() 再检查 = 崩溃 + 死代码）
# ============================================

contacts = {}

while True:
    print("1. 添加学生 2.查看所有 3.查找学生 4.修改成绩 5.删除学生 6.统计成绩 7.退出")
    if len(contacts) == 0:
        print("当前系统内容为空，请添加")
    else:
        print("当前系统内容：")
        for name, score in contacts.items():
            print(f"{name}:{score}")

    choice = input("请输入你的选择")

    # ---- 功能 1：添加学生（验证：先检查后转换）----
    if choice == "1":
        name = input("请输入学生姓名：")
        if name in contacts:
            print("该学生已存在，可用功能4修改")
        else:
            score_str = input("请输入学生成绩：")
            if not score_str.isdigit():          # ① 字符串阶段：检查数字
                print("成绩必须是数字！")
            else:
                score = int(score_str)           # ② 安全后才转换
                if score > 100 or score < 0:     # ③ 范围检查
                    print("成绩必须在 0~100 之间！")
                else:
                    contacts[name] = score       # ④ 通过才添加
                    print(f"已添加{name}")

    # ---- 功能 2：查看所有 ----
    elif choice == "2":
        for name, score in contacts.items():
            print(f"{name}的成绩是：{score}")

    # ---- 功能 3：查找学生 ----
    elif choice == "3":
        student = input("请输入你要查找的学生姓名：")
        if student in contacts:
            print(f"{student}的成绩是：{contacts[student]}")
        else:
            print("系统中没有该学生")

    # ---- 功能 4：修改成绩（同样的验证修复）----
    elif choice == "4":
        name1 = input("请输入你要修改的学生：")
        if name1 in contacts:
            new_str = input("请输入修改后的成绩：")
            if not new_str.isdigit():
                print("成绩必须是数字！")
            else:
                new_score = int(new_str)
                if new_score > 100 or new_score < 0:
                    print("成绩必须在 0~100 之间！")
                else:
                    contacts[name1] = new_score
                    print(f"{name1}的成绩已修改为{new_score}")
        else:
            print("系统中没有该学生！")

    # ---- 功能 5：删除学生 ----
    elif choice == "5":
        remove_name = input("请输入你要删除的学生：")
        if remove_name in contacts:
            del contacts[remove_name]
            print(f"{remove_name}已删除")
        else:
            print("系统中没有该学生")

    # ---- 功能 6：统计成绩 ----
    elif choice == "6":
        scores = list(contacts.values())
        if len(scores) == 0:
            print("当前系统内容为空，请输入")
        else:
            total = 0
            for s in scores:
                total = total + s
            average = total / len(scores)

            biggest = scores[0]
            smallest = scores[0]
            for s in scores:
                if s > biggest:
                    biggest = s
                if s < smallest:
                    smallest = s

            print(f"平均分是{average}")
            print(f"最高分是{biggest}")
            print(f"最低分是{smallest}")

    # ---- 功能 7：退出 ----
    elif choice == "7":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")
