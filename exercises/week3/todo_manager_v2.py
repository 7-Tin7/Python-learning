# ============================================
# 待办事项管理器（修正版 v2 —— 纯文本风格）
#
# 数据格式（关键设计！）：每行一个任务
#   任务内容 | 完成状态(0未完成/1已完成) | 时间
#   例：写周项目|0|2026-09-06 11:00
#
# 修正要点：
#   1. 时间在【每次添加时】取（不是程序开头取一次）
#   2. 数据格式加了完成状态位 → 功能3才有地方改
#   3. 标记/删除 = 读→改→写回
# ============================================

import os
from datetime import datetime

FILE_NAME = "任务清单.txt"     # 文件名常量（定义一次！）

while True:
    print("1.添加任务 2.查看任务 3.标记完成 4.删除任务 5.统计 6.退出")
    num = input("请输入你的选择：")

    # ---- 功能 1：添加任务 ----
    if num == "1":
        task = input("请输入你的任务：")
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M")   # ✅ 每次添加都取新时间！
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{task}|0|{time_str}\n")    # 新任务完成状态 = 0
        print("已保存任务")

    # ---- 功能 2：查看任务 ----
    elif num == "2":
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                parts = line.strip().split("|")          # 拆成 3 段
                mark = "[x]" if parts[1] == "1" else "[ ]"   # 按状态打勾
                print(f"{i + 1}. {mark} {parts[0]}（{parts[2]}）")
        else:
            print("还没有任务清单")

    # ---- 功能 3：标记完成（读→改→写回）----
    elif num == "3":
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):               # 先显示带编号的任务
                parts = line.strip().split("|")
                print(f"{i + 1}. {parts[0]}（{parts[2]}）")

            choice = input("请输入要标记完成的编号：")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(lines):
                    parts = lines[idx].strip().split("|")  # 拆开目标行
                    parts[1] = "1"                         # 完成状态改成 1
                    lines[idx] = "|".join(parts) + "\n"    # join 拼回一行
                    with open(FILE_NAME, "w", encoding="utf-8") as f:
                        for line in lines:                 # 写回整个文件
                            f.write(line)
                    print(f"已标记完成：{parts[0]}")
                else:
                    print("编号不存在")
            else:
                print("请输入数字")
        else:
            print("还没有任务清单")

    # ---- 功能 4：删除任务 ----
    elif num == "4":
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                parts = line.strip().split("|")
                print(f"{i + 1}. {parts[0]}（{parts[2]}）")

            choice = input("请输入要删除的编号：")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(lines):
                    removed = lines.pop(idx)               # pop 弹出那条
                    with open(FILE_NAME, "w", encoding="utf-8") as f:
                        for line in lines:
                            f.write(line)
                    name = removed.strip().split("|")[0]   # 取内容做提示
                    print(f"已删除：{name}")
                else:
                    print("编号不存在")
            else:
                print("请输入数字")
        else:
            print("当前还没有任务清单")

    # ---- 功能 5：统计 ----
    elif num == "5":
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                lines = f.readlines()
            total = len(lines)
            done_count = 0
            for line in lines:
                parts = line.strip().split("|")
                if parts[1] == "1":                        # 数已完成
                    done_count = done_count + 1
            print(f"总共 {total} 个任务，已完成 {done_count} 个，未完成 {total - done_count} 个")
        else:
            print("当前还没有任务清单")

    # ---- 功能 6：退出 ----
    elif num == "6" or num == "q":
        print("再见！")
        break

    else:
        print("无效的选择")
