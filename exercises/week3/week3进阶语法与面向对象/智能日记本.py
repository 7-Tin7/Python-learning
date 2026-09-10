import datetime
import os

while True:
    print("1.写日记 2.看日记 3.查看文件信息 4.删除日记 5.退出")
    choice = input("请输入你的选择")
    if choice == "1":
        note = input("今天想记点什么：")
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("日记.txt","a",encoding="utf-8") as f:
            f.write(f"[{time_str}] {note}\n")
        print("已保存!")
    elif choice == "2":
        if os.path.exists("日记.txt"):
            with open("日记.txt","r",encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
        else:
            print("还没有日记")
    elif choice == "3":
        if os.path.exists("日记.txt"):
            size = os.path.getsize("日记.txt")
            print(f"日记文件大小:{size}字节")
        else:
            print("还没有日记")
    elif choice == "4":
        if os.path.exists("日记.txt"):
            os.remove("日记.txt")
            print("日记删除成功")
        else:
            print("没有日记可删除")
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")





