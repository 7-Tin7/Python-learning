"""numbers = []
#收集数字
while True:
    num = input("请输入一个数字：/按q退出")
    if num == "q":
        break
    if not num.isdigit():
        print("请输入数字")
        continue
    numbers.append(int(num))
#计算数字
if len(numbers) == 0:
    print("还未输入任何数字")
else:
    total_sum = 0
    for n in numbers:
      total_sum = total_sum + n
    print(f"一共输入了{len(numbers)}个数字，总和等于{total_sum}")

    average = total_sum / len(numbers)
    print(f"平均值是{average}")

    biggest = numbers[0]
    for n in numbers:
      if n > biggest:
        biggest = n
    print(f"最大值为{biggest}")

    smallest = numbers[0]
    for n in numbers:
      if n < smallest:
        smallest = n
    print(f"最小值为{smallest}")"""











"""num_list = []
while True:
    num = input("请输入数字：/按q退出")
    if num == "q":
        break
    if not num.isdigit():
        print("请输入数字")
        continue
    num_list.append(int(num))
if len(num_list) == 0:
    print("还未输入任何数字，请输入数字")
else:
  total_sum = 0
  for n in num_list:
    total_sum = total_sum + n
  print(f"数字总和为{total_sum}")

  average = total_sum / len(num_list)
  print(f"平均值为{average}")

  biggest = num_list[0]
  for n in num_list:
      if n > biggest:
          biggest = n
  print(f"最大值为{biggest}")

  smallest = num_list[0]
  for n in num_list:
    if n < smallest:
      smallest = n
  print(f"最小值为{smallest}")"""







numbers = []
while True:
    num = input("请输入数字：/按q退出")
    if num == "q":
        break
    if not num.isdigit():
        print("当前输入的不是数字，请输入数字!")
        continue
    numbers.append(int(num))
if len(numbers) == 0:
    print("当前未输入数字")
else:
    total_sum = 0
    for n in numbers:
        total_sum = total_sum + n
    print(f"数字总和为{total_sum}")

    average = total_sum / len(numbers)
    print(f"数字平均值为{average}")

    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    print(f"输入数字的最大值为{biggest}")

    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    print(f"输入数字的最小值为{smallest}")


