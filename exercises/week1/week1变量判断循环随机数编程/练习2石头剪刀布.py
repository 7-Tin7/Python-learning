import random
player_score = 0
computer_score = 0
while True:
    player = input("请输入：石头/剪刀/布（输入q退出）：")
    if player == "q":
        print(f"你的最终得分{player_score}：电脑的最终得分{computer_score}")
        break
    computer = random.choice(["石头","剪刀","布"])
    if computer == player:
          print(f"你出了{player}，电脑出了{computer},平局！")
    elif (player == "石头" and computer == "剪刀") or\
         (player == "剪刀" and computer == "布") or\
         (player == "布" and computer == "石头"):
     player_score = player_score + 1
     print(f"你出了{player},电脑出了{computer},你赢了！")
    else:
     computer_score = computer_score + 1
     print(f"你出了{player}，电脑出了{computer}，你输了！")







#平局记入得分，双方各加一分
import random
player_score = 0
computer_score = 0
while True:
    player = input("石头/剪刀/布（按q退出）")
    if player == "q":
        print(f"你的最终得分{player_score}：电脑的最终得分{computer_score}")
        break
    computer =random.choice(["石头","剪刀","布"])
    if player == computer:
        print(f"你出了{player},电脑出了{computer},平局！")
        player_score = player_score +1
        computer_score = computer_score +1
    elif (player == "石头" and computer == "剪刀") or\
         (player == "剪刀" and computer == "布") or\
         (player == "布" and computer == "石头"):
        print(f"你出了{player},电脑出了{computer},你赢了！")
        player_score = player_score +1
    else:
        print(f"你出了{player},电脑出了{computer},你输了！")
        computer_score = computer_score +1


