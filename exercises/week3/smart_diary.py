# ============================================
# 第 3 周 练习：智能日记本（参考答案）📔✨
# ============================================

import os
from datetime import datetime

while True:
    print("\n1.写日记  2.看日记  3.查看文件信息  4.删除日记  5.退出")
    choice = input("请选择：")

    # ---- 功能 1：写日记（带时间戳）----
    if choice == "1":
        note = input("今天想记点什么：")
        now = datetime.now()                             # ① 当前时间对象
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")     # ② 格式化成字符串
        with open("日记.txt", "a", encoding="utf-8") as f:
            f.write(f"[{time_str}] {note}\n")            # ③ 时间+内容 存文件
        print("已保存！")

    # ---- 功能 2：看日记（os.path.exists 检查）----
    elif choice == "2":
        if os.path.exists("日记.txt"):                   # 文件存在才读
            with open("日记.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        else:
            print("还没有日记，先写一篇吧！")

    # ---- 功能 3：查看文件信息 ----
    elif choice == "3":
        if os.path.exists("日记.txt"):
            size = os.path.getsize("日记.txt")           # 文件字节数
            print(f"日记文件大小：{size} 字节")
        else:
            print("还没有日记文件")

    # ---- 功能 4：删除日记 ----
    elif choice == "4":
        if os.path.exists("日记.txt"):
            os.remove("日记.txt")                        # 删除文件
            print("日记已删除")
        else:
            print("没有日记可删")

    # ---- 功能 5：退出 ----
    elif choice == "5" or choice == "q":
        print("再见！")
        break

    # 兜底
    else:
        print("无效的选择，请重新输入")
