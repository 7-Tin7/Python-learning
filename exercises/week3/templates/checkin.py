# ============================================
# 第 3 周 练习：学习打卡记录器 📅
# 和"智能日记本"同款套路，巩固 os + datetime！
#
# 功能：打卡（带时间戳）→ 查看记录 → 统计打卡次数 → 退出
#
# 新知识：datetime / os（和上题一样）
# 旧知识：文件读写 / while / if-elif / input
# ============================================

import os
from datetime import datetime

while True:
    print("\n1.打卡  2.查看记录  3.统计打卡次数  4.退出")
    choice = input("请选择：")

    # ---- TODO 1：打卡（记录学习内容 + 时间戳）----
    # 如果 choice == "1"：
    #   thing = input("今天学习了什么：")
    #   time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #   with open("打卡记录.txt", "a", encoding="utf-8") as f:
    #       f.write(f"[{time_str}] {thing}\n")
    #   print("打卡成功！")

    # ---- TODO 2：查看记录 ----
    # 如果 choice == "2"：
    #   if os.path.exists("打卡记录.txt"):
    #       with open("打卡记录.txt", "r", encoding="utf-8") as f:
    #           for line in f:
    #               print(line.strip())
    #   else:
    #       print("还没有打卡记录")

    # ---- TODO 3：统计打卡次数 ----
    # 如果 choice == "3"：
    #   if os.path.exists("打卡记录.txt"):
    #       count = 0
    #       with open("打卡记录.txt", "r", encoding="utf-8") as f:
    #           for line in f:          # 每读一行 = 一条记录
    #               count = count + 1   # 累加套路！
    #       print(f"累计打卡 {count} 次，继续加油！")
    #   else:
    #       print("还没有打卡记录")

    # ---- TODO 4：退出 ----
    # 如果 choice == "4" 或 choice == "q"：打印"再见！"然后 break

    # 兜底：否则打印"无效的选择"

# 测试：
#   1. 打卡两次 → 查看记录 → 两条带时间戳的记录
#   2. 统计 → "累计打卡 2 次"
#   3. 关掉程序重开 → 记录还在（持久化！）
# ============================================
