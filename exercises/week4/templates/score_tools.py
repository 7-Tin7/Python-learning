# ============================================
# 第 4 周 练习 1：成绩快捷处理（参考答案）🚀
# ============================================

# 数据
scores = [92, 58, 85, 45, 76]
students = {"小明": 92, "小红": 58, "小刚": 76, "小丽": 45}

# ---- TODO 1：把所有成绩加 5 分 ----
bonus = [s + 5 for s in scores]
print(f"加分后：{bonus}")
# 输出：[97, 63, 90, 50, 81]

# ---- TODO 2：只保留及格的 ----
passed = [s for s in scores if s >= 60]
print(f"及格的：{passed}")
# 输出：[92, 85, 76]

# ---- TODO 3：找出不及格学生的名字 ----
fail = [name for name, s in students.items() if s < 60]
print(f"不及格的：{fail}")
# 输出：['小红', '小丽']

# ---- TODO 4：按成绩从高到低排名 ----
ranking = sorted(students.items(), key=lambda x: x[1], reverse=True)
for name, s in ranking:
    print(f"{name}: {s} 分")
# 输出：
#   小明: 92 分
#   小刚: 76 分
#   小红: 58 分
#   小丽: 45 分
