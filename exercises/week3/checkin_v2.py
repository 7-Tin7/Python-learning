# ============================================
# 学习打卡记录器 v2 📅（含删除单条记录）
#
# 功能：
#   1.打卡（带时间戳）  2.查看记录  3.统计次数
#   4.删除单条记录      5.清除全部  6.退出
# ============================================

import datetime
import os

while True:
    print("1.打卡 2.查看记录 3.统计次数 4.删除单条 5.清除全部 6.退出")
    choice = input("请输入你的选择")

    # ---- 功能 1：打卡 ----
    if choice == "1":
        content = input("请输入今天要学习的内容：")
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("学习内容.txt", "a", encoding="utf-8") as f:
            f.write(f"{time_str} 学习了{content}\n")
        print("已保存")

    # ---- 功能 2：查看记录 ----
    elif choice == "2":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        else:
            print("当前没有打卡记录")

    # ---- 功能 3：统计次数（从文件数！）----
    elif choice == "3":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt", "r", encoding="utf-8") as f:
                count = 0
                for line in f:
                    count = count + 1
            print(f"一共打卡了{count}次")
        else:
            print("当前没有打卡记录")

    # ---- 功能 4：删除单条（读→删→重写）----
    elif choice == "4":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()          # ① 全部读进列表

            for i, line in enumerate(lines):   # ② 带编号显示
                print(f"{i + 1}. {line.strip()}")

            num = input("请输入要删除的编号：")
            if num.isdigit():
                idx = int(num) - 1             # ③ 编号→索引（从0开始）
                if 0 <= idx < len(lines):
                    removed = lines.pop(idx)   # ④ 弹出那一条
                    with open("学习内容.txt", "w", encoding="utf-8") as f:
                        for line in lines:     # ⑤ 剩下的重写回去
                            f.write(line)      #    行自带 \n，不用再加
                    print(f"已删除：{removed.strip()}")
                else:
                    print("编号不存在")
            else:
                print("请输入数字编号")
        else:
            print("没有记录可删")

    # ---- 功能 5：清除全部 ----
    elif choice == "5":
        if os.path.exists("学习内容.txt"):
            os.remove("学习内容.txt")
            print("已清除全部打卡记录")
        else:
            print("当前没有打卡记录")

    # ---- 功能 6：退出 ----
    elif choice == "6" or choice == "q":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
