# ============================================
# 练习 2：石头剪刀布（参考答案）
# ============================================

import random

# ---- TODO 1：计分 ----
player_score = 0
computer_score = 0

# ---- TODO 2：主循环 ----
while True:

    # ---- TODO 3：玩家出拳 ----
    player = input("请输入：石头 / 剪刀 / 布（输入 q 退出）：").strip()

    if player == "q":
        print(f"最终比分 你 {player_score} : {computer_score} 电脑")
        break  # 退出游戏

    # ---- TODO 4：电脑出拳 ----
    computer = random.choice(["石头", "剪刀", "布"])

    # ---- TODO 5：判断胜负 ----
    if player == computer:
        # 平局：两人出的一样
        print(f"你出了{player}，电脑出了{computer}，平局！")
    elif (player == "石头" and computer == "剪刀") or \
         (player == "剪刀" and computer == "布") or \
         (player == "布" and computer == "石头"):
        # 你赢的 3 种情况，用 or 连成一行
        player_score = player_score + 1
        print(f"你出了{player}，电脑出了{computer}，你赢了！")
    else:
        # 剩下的情况都是电脑赢
        computer_score = computer_score + 1
        print(f"你出了{player}，电脑出了{computer}，电脑赢了！")

    print(f"当前比分 你 {player_score} : {computer_score} 电脑")
