contacts = {"小明": 92, "小红": 85}

print("写法 A：for score, name in contacts.items()")
for score, name in contacts.items():
    print(f"  score 变量里装的是：{score}   ← 姓名！")
    print(f"  name 变量里装的是：{name}   ← 成绩！")

print()
print("写法 B：for name, score in contacts.items()")
for name, score in contacts.items():
    print(f"  name 变量里装的是：{name}   ← 姓名")
    print(f"  score 变量里装的是：{score}   ← 成绩")
