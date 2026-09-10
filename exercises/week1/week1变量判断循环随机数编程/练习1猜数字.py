"""import random
secret = random.randint(1,100)
guesses = 0
while True:
  guess = int(input("请输入你猜的数字"))
  guesses = guesses + 1
  if guess > secret:
       print("太大了")
  elif guess < secret:
       print("太小了")
  else:
       print(f"恭喜你,猜了{guesses}次")
  break"""


import random
secret = random.randint(1, 100)
guesses = 0
while True:
    guess = input(f"请输入你猜的数字:/按q退出")
    if guess == "q" and guess == secret:
        print(f"本次共猜了{guesses}次,最终猜对")
    elif guess == "q" and guess != secret:
        print(f"本次共猜了{guesses}次，最终没猜对")
        break
    if guess == "提示":
        print(f"数字范围在1~100之间")
        continue
    guess = int(guess)
    guesses = guesses + 1
    if guess > secret:
        print(f"你猜的数字太大了")
    elif guess < secret:
        print(f"你猜的数字太小了")
    else:
        print(f"你猜对了！本次一共猜了{guesses}次")



































