import numpy as np
scores = np.array([92, 58, 85, 45, 76, 88, 61, 39, 95, 70])
new = scores + 5
choose = scores[(scores >= 60)]
average = scores.sum()/len(scores)
choose1 = len(scores[(scores < 60)])
print(f"成绩数组:{scores}\n加分后:{new}\n及格的成绩:{choose}\n平均分:{average}\n不及格的人数：{choose1}")


import numpy as np
scores = np.array([92, 58, 85, 45, 76, 88, 61, 39, 95, 70])
new = scores + 5
passed = scores[(scores >= 60)]
average = scores.mean()
fail_count = len(scores[scores < 60])
print(f"成绩数组:{scores}\n加分后:{new}\n及格的成绩:{choose}\n平均分:{average}\n不及格的人数：{choose1}")
