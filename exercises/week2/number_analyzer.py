# ============================================
# 第 2 周 练习 2：数字统计器（参考答案）🔢
# ============================================

numbers = []  # 空列表，用来存输入的数字

# ---- TODO 1：收集数字 ----
while True:
    num = input("请输入一个数字（输入 q 结束）：")
    if num == "q":
        break
    if not num.isdigit():
        print("请输入数字！")
        continue
    numbers.append(int(num))

# ---- TODO 2：处理空列表 ----
if len(numbers) == 0:
    print("你没有输入任何数字")
else:
    # ---- TODO 3：算总和（累加套路）----
    total_sum = 0
    for n in numbers:
        total_sum = total_sum + n
    print(f"一共输入了 {len(numbers)} 个数字，总和是 {total_sum}")

    # ---- TODO 4：算平均值 ----
    average = total_sum / len(numbers)
    print(f"平均值是 {average}")

    # ---- TODO 5：找最大值（擂台套路）----
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    print(f"最大的是 {biggest}")

    # ---- TODO 6：找最小值（擂台套路）----
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    print(f"最小的是 {smallest}")
