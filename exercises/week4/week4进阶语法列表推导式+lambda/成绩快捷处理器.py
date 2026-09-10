scores = [92, 58, 85, 45, 76]
students = {"小明": 92, "小红": 58, "小刚": 76, "小丽": 45}
bonus = [s+5 for s in scores]
passed = [s for s in scores if s >= 60]
fail = [name for name, s in students.items() if s < 60]
ranking = sorted(students.items(),key = lambda x:x[1],reverse=True)
print(bonus)
print(passed)
print(fail)
print(ranking)