# ============================================
# 🏫 周项目：学生成绩管理系统
#
# 功能：
#   1. 添加学生    2. 查看所有    3. 查找学生
#   4. 修改成绩    5. 删除学生    6. 统计成绩
#   7. 退出
#
# 用到：字典 / 函数 / while / if-elif-else / 累加和擂台套路
# 项目说明书：notes/week2/week_project_grade_system.md
# ============================================

# ---- 功能 1：添加学生 ----
def add_student(students):
    name = input("请输入学生姓名：")
    if name in students:
        print(f"{name} 已存在，请用【修改成绩】功能")
        return                       # 提前结束函数

    score_str = input(f"请输入 {name} 的成绩：")
    if not score_str.isdigit():
        print("成绩必须是数字！")
        return
    score = int(score_str)
    if score < 0 or score > 100:
        print("成绩必须在 0~100 之间！")
        return

    students[name] = score           # 键不存在 → 添加
    print(f"已添加：{name} → {score} 分")

# ---- 功能 2：查看所有 ----
def show_all(students):
    if len(students) == 0:
        print("系统中还没有学生")
        return
    print("===== 学生成绩表 =====")
    for name, score in students.items():
        print(f"{name}: {score} 分")
    print("=====================")

# ---- 功能 3：查找学生 ----
def find_student(students):
    name = input("请输入要查找的学生姓名：")
    if name in students:
        print(f"{name} 的成绩是：{students[name]} 分")
    else:
        print(f"系统中没有 {name}")

# ---- 功能 4：修改成绩 ----
def update_score(students):
    name = input("请输入要修改的学生姓名：")
    if name not in students:
        print(f"系统中没有 {name}")
        return

    score_str = input(f"请输入 {name} 的新成绩：")
    if not score_str.isdigit():
        print("成绩必须是数字！")
        return
    score = int(score_str)
    if score < 0 or score > 100:
        print("成绩必须在 0~100 之间！")
        return

    students[name] = score           # 键存在 → 覆盖（修改！）
    print(f"已修改：{name} → {score} 分")

# ---- 功能 5：删除学生 ----
def delete_student(students):
    name = input("请输入要删除的学生姓名：")
    if name in students:
        del students[name]           # del 删除键值对
        print(f"已删除 {name}")
    else:
        print(f"系统中没有 {name}")

# ---- 功能 6：统计成绩 ----
def show_stats(students):
    if len(students) == 0:
        print("系统中还没有学生，无法统计")
        return

    # 用 values() 取出所有成绩
    scores = list(students.values())     # [92, 85, 76]

    # 累加套路：算总分
    total = 0
    for s in scores:
        total = total + s
    average = total / len(scores)

    # 擂台套路：找最高最低
    highest = scores[0]
    lowest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s

    print(f"学生人数：{len(scores)}")
    print(f"平均分：{average}")
    print(f"最高分：{highest}")
    print(f"最低分：{lowest}")

# ---- 主程序 ----
students = {}                        # 姓名 → 成绩

while True:
    print("\n===== 学生成绩管理系统 =====")
    print("1.添加学生  2.查看所有  3.查找学生")
    print("4.修改成绩  5.删除学生  6.统计成绩  7.退出")
    choice = input("请选择：")

    if choice == "1":
        add_student(students)        # 调用函数！
    elif choice == "2":
        show_all(students)
    elif choice == "3":
        find_student(students)
    elif choice == "4":
        update_score(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        show_stats(students)
    elif choice == "7" or choice == "q":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")
