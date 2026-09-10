# ============================================
# 练习 1：猜数字游戏（参考答案）
# ============================================

import random

# ---- TODO 1：生成随机数 ----
# random.randint(1, 100) 会在 1~100 之间随机选一个整数
secret = random.randint(1, 100)

# ---- TODO 2：记录猜的次数 ----
guesses = 0

# ---- TODO 3：主循环 ----
while True:
    # 1. 玩家输入（input 返回字符串，int() 转成整数）
    guess = int(input("请输入你猜的数字："))

    # 2. 猜的次数加 1
    guesses = guesses + 1

    # 3. 比较大小
    if guess > secret:
        print("太大了！")
    elif guess < secret:
        print("太小了！")
    else:
        # f-string：把 {guesses} 替换成实际的数字
        print(f"恭喜你！猜了 {guesses} 次！")
        break  # 猜对了，跳出循环
