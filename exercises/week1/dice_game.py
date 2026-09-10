# ============================================
# 练习 3：掷骰子大战 🎲（参考改进版）
# 第 1 周 · Python 基础
#
# 游戏规则：
#   你和电脑各掷一个骰子（1~6 点），点数大的赢，点数相同算平局。
#   玩到输入 q 退出，退出时显示最终比分。
#
# 改进功能：
#   1. 输入超出 1~6 范围 → 提示并重新输入（continue）
#   2. 输入不是数字 → 提示并重新输入（isdigit）
# ============================================

import random

player_score = 0
computer_score = 0

while True:
    player = input("请输入骰子数(1~6)/输入q退出:")

    # 先处理退出
    if player == "q":
        print(f"你的最终得分{player_score}:电脑的最终得分{computer_score}")
        break

    # 再检查是不是数字（防止 int() 崩溃）
    if not player.isdigit():
        print("请输入数字！")
        continue

    player = int(player)

    # 检查范围，超出就重新输入
    if player > 6 or player < 1:
        print("请输入正确范围的骰子数字！")
        continue

    # 到这里，输入一定是 1~6 的合法数字
    computer = random.randint(1, 6)

    if player == computer:
        print(f"你的数字{player},电脑的数字{computer},一样大！")
        player_score = player_score + 1
        computer_score = computer_score + 1
    elif player > computer:
        print(f"你的数字{player},电脑的数字{computer},你大！")
        player_score = player_score + 1
    else:
        print(f"你的数字{player},电脑的数字{computer},电脑大！")
        computer_score = computer_score + 1
