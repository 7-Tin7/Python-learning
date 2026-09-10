"""ages = set()
name_storage = []
for x in range(3):
    name = input("请输入好友姓名:")
    age = int(input(f"请输入{name}的年龄："))
    name_storage.append((name,age))

for name,age in name_storage:
    print(f"{name}的年龄是{age}")
for name,age in name_storage:
    ages.add(age)
print(f"共有{len(ages)}种不同年龄：{ages}")"""



"""ages = set()
friends = []
for x in range(3):
    name = input("请输入好友的姓名:")
    age = int(input(f"请输入{name}的年龄:"))
    friends.append((name,age))

for name,age in friends:
    print(f"{name}的年龄是{age}")
for name,age in friends:
    ages.add(age)
print(f"共有{len(ages)}种不同年龄:{ages}")"""


friends = []
ages = set()
for x in range(3):
    name = input("请输入好友姓名")
    age = int(input(f"请输入{name}年龄:"))
    friends.append((name,age))
for name,age in friends:
    print(f"{name}的年龄是{age}")
for name,age in friends:
    ages.add(age)
print(f"共有{len(ages)}种不同年龄：{ages}")

