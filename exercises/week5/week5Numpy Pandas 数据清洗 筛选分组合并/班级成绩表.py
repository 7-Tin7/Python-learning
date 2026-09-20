import numpy as np
scores = np.array([
    [92, 85, 78],   # 学生1（语文 数学 英语）
    [58, 90, 65],   # 学生2
    [85, 45, 88],   # 学生3
    [76, 76, 76],   # 学生4
    [95, 88, 92],   # 学生5
])
print(f"形状：{scores.shape}")
print(f"取行{scores[0]} 取列{scores[:,0]}")
print(f"每个学生的平均分:{scores.mean(axis=1)}")
print(f"每门课平均分{scores.mean(axis=0)}")
passed = scores[scores >= 60]
percent = len(passed) / scores.size
print(f"全班及格成绩{passed}，全班及格率{percent:.1%}")
fixed = np.where(scores < 60,0,scores)
print(f"不及格记0分:\n{fixed}")

