while True:
    print("1 写(追加)日记 2.读日记 3.退出")
    num = input("请输入选择")
    if num == "1":
        note = input("请输入今天想写的内容：")
        with open("日记.txt","a",encoding="utf-8") as f:
            f.write(note + "\n")
        print("已保存!")
    elif num == "2":
        try:
            with open("日记.txt","r",encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("还没有日记，先写一篇吧")
    elif num == "3":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")


