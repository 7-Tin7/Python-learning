contacts = {}
while True:
    print("1. 添加学生 2.查看所有 3.查找学生 4.修改成绩 5.删除学生 6.统计成绩 7.退出")
    if len(contacts) == 0:
        print("当前系统内容为空，请添加")
    else:
        print("当前系统内容：")
        for name,score in contacts.items():
            print(f"{name}:{score}")
    choice = input("请输入你的选择")
    if choice == "1":
        name = input("请输入学生姓名：")
        if name in contacts:
            print("该学生已存在")
        else:
            score_str = input("请输入学生成绩：")
            if not score_str.isdigit():
                print("请输入数字")
            else:
                score = int(score_str)
                if score > 100 or score < 0:
                    print("成绩范围需要在0~100之间")
                else:
                    contacts[name] = score
                    print(f"已添加{name}")
    elif choice == "2":
        for name,score in contacts.items():
            print(f"{name}的成绩是：{score}")
    elif choice == "3":
        student = input("请输入你要查找的学生姓名：")
        if student in contacts:
            print(f"{student}的成绩是：{contacts[student]}")
        else:
            print("系统中没有该学生")
    elif choice == "4":
        name1 = input("请输入你要修改的学生：")
        if name1 in contacts:
            new_score_str = input("请输入修改后的成绩：")
            if not new_score_str.isdigit():
                print("请输入数字")
            else:
                new_score = int(new_score_str)
                if new_score > 100 or new_score < 0:
                    print("成绩范围需要在0~100之间")
                else:
                    contacts[name1] = new_score
                    print(f"{name1}的成绩已修改为{new_score}")
        else:
            print("系统中他没有该学生！")
    elif choice == "5":
        remove_name = input("请输入你要删除的学生：")
        if remove_name in contacts:
            del contacts[remove_name]
            print(f"{remove_name}已删除")
        else:
            print("系统中没有该学生")
    elif choice == "6":
        score1 = list(contacts.values())
        if len(score1) == 0:
            print("当前系统内容为空，请输入")
        else:
            total = 0
            for s in score1:
                total = total + s
            average = total / len(score1)
            biggest = score1[0]
            smallest = score1[0]
            for s in score1:
                if s > biggest:
                    biggest = s
                if s < smallest:
                    smallest = s
            print(f"平均分是{average}")
            print(f"最高分是{biggest}")
            print(f"最低分是{smallest}")
    elif choice == "7":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")




