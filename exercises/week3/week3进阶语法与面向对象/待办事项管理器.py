import datetime
import os
while True:
    print("1.添加任务 2.查看任务时间 3.标记完成 4.删除任务 5.统计所有任务 6.退出")
    num = input("请输入你的选择")
    if num == "1":
        task = input("请输入你的任务")
        now = datetime.datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("任务清单.txt","a",encoding="utf-8") as f:
            f.write(f"{time_str} {task}\n")
            print("已保存任务")
    elif num == "2":
        if os.path.exists("任务清单.txt"):
            with open("任务清单.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
                for i,line in enumerate(lines):
                    print(f"{i+1} {line.strip()}")
                times = input("请选择你要查看的任务编号")
                if times.isdigit():
                    idx = int(times) - 1
                    if 0 <= idx <len(lines):
                        with open("任务清单.txt","w",encoding="utf-8") as f:
                            for line in lines:
                                f.write(line)
                        print(f"该任务的时间是{time_str}")
                    else:
                        print("任务清单没有该任务")
                else:
                    print("请输入数字")
        else:
            print("还没有任务清单")
    elif num == "3":
            if os.path.exists("任务清单.txt"):
                with open("任务清单.txt","r",encoding="utf-8") as f:
                    lines = f.readlines()
                for i,line in enumerate(lines):
                    parts = line.strip().split("|")
                    print(f"{i+1}. {parts[0]}（{parts[2]}）")
                masks = input("请输入你要标记的任务编号")
                if masks.isdigit():
                    idx = int(masks) - 1
                    if 0 <= idx < len(lines):
                        parts = lines[idx].strip().split("|")
                        parts[1] = "1"
                        lines[idx] = "|".join(parts) + "\n"
                        with open("任务清单.txt","r",encoding="utf-8") as f:
                            for line in lines:
                                f.write(line)
                            print(f"已标记完成,记为{parts[0]}")
                    else:
                        print("编号不存在")
                else:
                    print("请输入数字")
            else:
                print("不存在任务清单")
    elif num == "4":
        if os.path.exists("任务清单.txt"):
            with open("任务清单.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
                for i,line in enumerate(lines):
                    print(f"{i+1} {line.strip()}")
                num1 = input("请输入要删除的任务编号:")
                if num1.isdigit():
                    idx = int(num) - 1
                    if 0 <= idx < len(lines):
                        removed = task.pop(idx)
                        with open("任务清单","w",encoding="utf-8"):
                            for line in lines:
                                f.write(line)
                        print(f"已删除{num1}")
                    else:
                        print("任务清单中没有该编号")
                else:
                    print("输入的不是数字")
        else:
            print("当前还未存在任务清单")
    elif num == "5":
        try:
            if os.path.exists("任务清单.txt"):
                with open("任务清单","r",encoding="utf-8") as f:
                    count = 0
                    for task in f:
                        count = count + 1
                print(f"一共有{count}个任务")
        except FileNotFoundError:
            print("当前没有任务清单")
    elif num == "6":
        print("再见！")
        break
    else:
        print("无效的选择")






