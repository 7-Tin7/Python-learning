# ============================================
# 第 5 周 练习 1：NumPy 成绩分析 📊
#
# 对比体验：你第 2 周手写的"数字统计器"用了 30+ 行，
#          用 NumPy 只要 5 行！
#
# 新知识：NumPy 数组 / 向量化运算 / 布尔索引 / 统计函数
# 旧知识：列表、print、f-string
# ============================================

import numpy as np

# 一个班的成绩
scores = np.array([92, 58, 85, 45, 76, 88, 61, 39, 95, 70])

# ---- TODO 1：认识数组 ----
# print(f"成绩数组：{scores}")
# print(f"形状：{scores.shape}，个数：{len(scores)}")
# print(f"数据类型：{scores.dtype}")

# ---- TODO 2：全班加分 5 分（向量化运算！不用循环）----
# new_scores = scores + 5
# print(f"加分后：{new_scores}")

# ---- TODO 3：用布尔索引筛出及格的成绩 ----
# passed = scores[scores >= 60]
# print(f"及格的成绩：{passed}")

# ---- TODO 4：统计（一行一个！）----
# print(f"总分：{scores.sum()}")
# print(f"平均分：{scores.mean()}")
# print(f"最高分：{scores.max()}")
# print(f"最低分：{scores.min()}")

# ---- TODO 5：数一下不及格的有几个 ----
# fail = scores[scores < 60]        # 先筛出不及格的
# print(f"不及格人数：{len(fail)}")
# 提示：也可以一步到位：np.sum(scores < 60)
#       （True 当 1，False 当 0 相加 = 个数）

# ---- 挑战（可选）：找出 60~90 分之间的成绩 ----
# 提示：组合条件要用 & 且每个条件加括号
# mid = scores[(scores >= 60) & (scores <= 90)]

# 示例输出：
#   成绩数组：[92 58 85 45 76 88 61 39 95 70]
#   加分后：[97 63 90 50 81 93 66 44 100 75]
#   及格的成绩：[92 85 76 88 61 95 70]
#   平均分：70.9
#   不及格人数：3
# ============================================
