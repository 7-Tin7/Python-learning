import datetime
import os
times = 0
while True:
    print("1.打卡 2.查看记录 3.统计打卡次数 4.清除打卡记录 5.退出 6.删除某条打卡记录")
    choice = input("请输入你的选择")
    if choice == "1":
        content = input("请输入今天要学习的内容：")
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("学习内容.txt","a",encoding="utf-8") as f:
            f.write(f"{time_str} 学习了{content}\n")
            print("已保存")
    elif choice == "2":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt","r",encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        else:
            print("当前没有打卡记录")
    elif choice == "3":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt","r",encoding="utf-8") as f:
                count = 0
                for line in f:
                    count = count + 1
                print(f"一共打卡了{count}次")
    elif choice == "4":
        if os.path.exists("学习内容.txt"):
            os.remove("学习内容.txt")
            print("已清除当前打卡记录")
    elif choice == "5":
        print("再见！")
        break
    elif choice == "6":
        if os.path.exists("学习内容.txt"):
            with open("学习内容.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
            for i,line in enumerate(lines):
                print(f"{i+1}.{line.strip()}")
            num = input("请输入你要删除记录的编码")
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(lines):
                    removed = lines.pop(idx)
                    with open("学习内容.txt","w",encoding="utf-8") as f:
                        for line in lines:
                            f.write(line)
                    print("已删除")
                else:
                    print("编号不存在")
            else:
                print("请输入数字编号")
        else:
            print("没有记录可删")
    else:
        print("无效的选择，请重新输入")

