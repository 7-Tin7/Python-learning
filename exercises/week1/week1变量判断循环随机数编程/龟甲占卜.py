import random
success_time = 0
fail_time = 0
equal_time = 0
while True:
    num = input("请输入你心中想的任意数字（数字位数：1~5位）:/按q退出")
    if num == "q":
        print(f"本次占卜之事您的成功次数为:{success_time},失败次数为:{fail_time},神明拿不定注意次数为:{equal_time}")
        if success_time < fail_time:
            print(f"成功概率较低，建议您再三思索之后再去做这件事情")
        else:
            print(f"成功概率较高，可以大胆且仔细去完成这件事情")
        break
    num = int(num)
    if num >10000 or num <1:
        print(f"该数字不在范围内，请重新输入")
        continue
    secret = random.randint(1, 10000)
    if num == secret:
        print("此事犹豫不决，不予建议")
        equal_time = equal_time + 1
    elif num < secret:
        print("此事大概率失败")
        fail_time = fail_time + 1
    else:
        print("此事大概率成功")
        success_time = success_time + 1