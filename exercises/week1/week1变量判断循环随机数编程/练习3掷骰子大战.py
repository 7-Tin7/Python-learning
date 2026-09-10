import random
player_score = 0
computer_score = 0
while True:
    player = input("请输入骰子数(1~6)/输入q退出:")
    if player == "q":
        print(f"你的最终得分{player_score}:电脑的最终得分{computer_score}")
        break
    player = int(player)
    computer = random.randint(1,6)
    if player > 6 or player <1:
        print(f"请输入正确范围骰子的数字")
        continue
    if player == computer:
        print(f"你的数字{player},电脑的数字{computer},一样大！")
        player_score = player_score + 1
        computer_score = computer_score + 1
    elif player > computer:
        print(f"你的数字{player},电脑的数字{computer},你大！")
        player_score = player_score +1

    else:
        print(f"你的数字{player},电脑的数字{computer},电脑大！")
        computer_score = computer_score +1
