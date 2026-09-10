"""person = []
numbers = set()
while True:
    if len((person,numbers)) == 0:
        print("当前通讯录为空，请添加联系人")
    else:
        print("1.添加联系人 2.查找电话 3.查看所有 4.退出")
        choice = input("请输入选择:")
        if choice == "1":
            new_person = input("请输入要添加的联系人姓名:")
            new_number = input(f"请输入{new_person}的电话:")
            person.append((new_person,new_number))
            numbers.add(new_number)
        elif choice == "2":
            number = input("请输入你要查找的电话:")
            if number in numbers:
                print(f"该电话联系人是{new_person}")
            else:
                print("该号码不存在通讯录中")
        elif choice == "3":
            for new_person,new_number in person:
                print(f"{new_person}的电话号码是:{new_number}")
        elif choice == "4":
            print("退出通讯录，再见！")
            break
        else:
            print("无效的选择，请重新输入")"""




contacts = {}
while True:
    if len(contacts) == 0:
        print("当前通讯录为空，请添加联系人")
    else:
        print("当前通讯录:")
        for num,name in contacts.items():
            print(f"{name}:{num}")
    print("1.添加联系人 2.查找电话 3.查看所有 4.退出")
    choice = input("请输入选择:")
    if choice == "1":
        new_person = input("请输入要添加的联系人姓名:")
        new_number = input(f"请输入{new_person}的电话:")
        contacts[new_number] = new_person
        print(f"已添加{new_person}")
    elif choice == "2":
        number = input("请输入你要查找的电话:")
        if number in contacts:
            print(f"该电话联系人是{contacts[number]}")
        else:
            print("该号码不存在通讯录中")
    elif choice == "3":
        for num,name in contacts.items():
            print(f"{name}的电话号码是:{num}")
    elif choice == "4":
        print("退出通讯录，再见！")
        break
    else:
        print("无效的选择，请重新输入")