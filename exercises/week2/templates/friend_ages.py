# ============================================
# 第 2 周 练习：好友年龄统计器（参考答案）👥
# ============================================

friends = []   # 用来存元组的列表
ages = set()   # 用来存年龄的集合（自动去重）

# ---- TODO 1：录入 3 个好友 ----
for x in range(3):                    # range(3) = 0,1,2，循环 3 次
    name = input("请输入好友名字：")
    age = int(input(f"{name} 的年龄："))
    friends.append((name, age))       # 双层括号：(name, age) 是元组，append 是列表操作

# ---- TODO 2：打印所有好友 ----
for name, age in friends:             # 拆包：从元组里取出 name 和 age
    print(f"{name}今年{age}岁")

# ---- TODO 3：把年龄收集进集合 ----
for name, age in friends:
    ages.add(age)                     # 重复的年龄自动去重

# ---- TODO 4：显示去重结果 ----
print(f"共有 {len(ages)} 种不同年龄：{ages}")
