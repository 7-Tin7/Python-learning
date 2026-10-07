# ============================================
# 🏆 周项目：待办事项管理器（第 3 周毕业作品）
#
# 功能：
#   1.添加任务  2.查看任务  3.标记完成
#   4.删除任务  5.统计    6.退出
#
# 技术：class Task + 文件读写 + datetime + FILE_NAME 常量
# 项目说明书：notes/week3/week_project_todo.md
# ============================================

import os
from datetime import datetime

FILE_NAME = "任务.txt"          # 文件名常量：定义一次，处处引用！


class Task:
    """一个待办任务"""
    def __init__(self, content, done=False, created_at=None):
        self.content = content                # 任务内容
        self.done = done                      # 是否完成（True/False）
        if created_at is None:                # 没给时间就自动记录
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.created_at = created_at          # 创建时间（字符串）


# ---- 加载：文件 → Task 列表 ----
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                # TODO 1：把一行文字还原成 Task
                # parts = line.strip().split("|")
                # content = parts[0]
                # done = (parts[1] == "1")     # "1" → True
                # created_at = parts[2]
                # tasks.append(Task(content, done, created_at))
                pass
    return tasks


# ---- 保存：Task 列表 → 文件 ----
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            # TODO 2：把 Task 写成一行
            # f.write(f"{t.content}|{1 if t.done else 0}|{t.created_at}\n")
            pass


# ---- 显示所有任务（带编号）----
def show_tasks(tasks):
    if len(tasks) == 0:
        print("还没有任务，添加一个吧！")
        return
    print("===== 任务清单 =====")
    for i, t in enumerate(tasks):
        mark = "[x]" if t.done else "[ ]"      # 完成打 x
        print(f"{i + 1}. {mark} {t.content}（{t.created_at}）")


# ---- 让用户选编号（返回索引，或 -1 表示无效）----
def choose_index(tasks, prompt):
    show_tasks(tasks)
    num = input(prompt)
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(tasks):
            return idx
    print("编号无效！")
    return -1


# ---- 主程序 ----
tasks = load_tasks()            # 启动时加载一次！

while True:
    print("\n1.添加任务 2.查看任务 3.标记完成 4.删除任务 5.统计 6.退出")
    choice = input("请选择：")

    # ---- 功能 1：添加任务 ----
    if choice == "1":
        content = input("请输入任务内容：")
        tasks.append(Task(content))     # 创建 Task 对象，时间自动记录
        save_tasks(tasks)               # 立刻存盘
        print("已添加！")

    # ---- 功能 2：查看任务 ----
    elif choice == "2":
        show_tasks(tasks)

    # ---- 功能 3：标记完成 ----
    elif choice == "3":
        if len(tasks) == 0:
            print("还没有任务")
        else:
            idx = choose_index(tasks, "请输入要标记完成的编号：")  # ① 选编号
            if idx != -1:                                        # ② 编号有效？
                tasks[idx].done = True                            # ③ 改对象属性！
                save_tasks(tasks)                                 # ④ 存盘
                print(f"已标记完成：{tasks[idx].content}")

    # ---- 功能 4：删除任务 ----
    elif choice == "4":
        if len(tasks) == 0:
            print("还没有任务")
        else:
            # TODO 4：选编号 → 删除 → 保存
            # idx = choose_index(tasks, "请输入要删除的编号：")
            # if idx != -1:
            #     removed = tasks.pop(idx)
            #     save_tasks(tasks)
            #     print(f"已删除：{removed.content}")
            pass

    # ---- 功能 5：统计 ----
    elif choice == "5":
        # TODO 5：统计总数/完成数/未完成数
        # total = len(tasks)
        # done_count = 0
        # for t in tasks:
        #     if t.done:
        #         done_count = done_count + 1
        # print(f"总共 {total} 个，已完成 {done_count} 个，未完成 {total - done_count} 个")
        pass

    # ---- 功能 6：退出 ----
    elif choice == "6" or choice == "q":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
