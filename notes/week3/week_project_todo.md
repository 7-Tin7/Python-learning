# 🏆 周项目说明书：待办事项管理器（第 3 周毕业作品）

## 一、功能需求

1. **添加任务**：输入任务内容，自动记录创建时间
2. **查看任务**：显示编号、完成状态（[x]完成/[ ]未完成）、内容、创建时间
3. **标记完成**：按编号把任务标成已完成
4. **删除任务**：按编号删除某条任务
5. **统计**：总共几个任务、已完成几个、未完成几个
6. **退出**

## 二、核心技术（第 3 周知识总检阅）

| 技术 | 用在哪 |
|------|--------|
| **class Task** | 每个任务 = 一个对象（内容/完成状态/创建时间）|
| **文件读写** | 任务存 `任务.txt`，重启还在（持久化）|
| **读-改-写回** | 标记完成/删除后重写文件（打卡记录器刚练过！）|
| **datetime** | 添加任务时自动记录时间 |
| **try/except** | 输入不合法不崩溃（可选加分）|
| **FILE_NAME 常量** | 文件名定义一次处处引用（上节课学的！）|

## 三、Task 类设计

```python
class Task:
    def __init__(self, content, done=False, created_at=None):
        self.content = content            # 任务内容（字符串）
        self.done = done                  # 是否完成（True/False）
        if created_at is None:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.created_at = created_at      # 创建时间（字符串）
```

## 四、数据存储格式（一行一个任务，用 | 分隔）

文件里每行存一个任务：
```
写周项目|0|2026-09-06 10:30
买菜|1|2026-09-06 09:00
```

| 第 1 段 | 第 2 段 | 第 3 段 |
|--------|--------|--------|
| 任务内容 | 完成状态（0=未完成，1=已完成）| 创建时间 |

存的时候（Task → 一行）：
```python
f.write(f"{t.content}|{1 if t.done else 0}|{t.created_at}\n")
```

读的时候（一行 → Task）：
```python
parts = line.strip().split("|")   # 按 | 拆成 3 段
content = parts[0]
done = (parts[1] == "1")          # "1" 转成 True
created_at = parts[2]
tasks.append(Task(content, done, created_at))
```

## 五、程序结构（推荐）

```python
class Task:                 # 任务类
    ...

def load_tasks():           # 文件 → Task 列表
    ...

def save_tasks(tasks):      # Task 列表 → 文件（w 覆盖）

tasks = load_tasks()        # 启动时加载一次

while True:                 # 菜单循环
    # 1 添加 → tasks.append(Task(...)) → save_tasks(tasks)
    # 2 查看 → for 循环带编号显示
    # 3 标记完成 → 找编号 → tasks[i].done = True → save_tasks(tasks)
    # 4 删除 → 找编号 → tasks.pop(i) → save_tasks(tasks)
    # 5 统计 → len(tasks) + 数 done 的数量
```

**关键思路**：程序启动时把文件**全部读进内存**（tasks 列表），
每次改动后**整体写回文件**——简单可靠。

## 六、测试清单

- [ ] 添加"写周项目" → 查看显示 [ ] 写周项目 + 时间
- [ ] 添加"买菜" → 共 2 条
- [ ] 标记第 1 条完成 → 查看显示 [x]
- [ ] 统计 → 总共 2，完成 1，未完成 1
- [ ] 删除第 1 条 → 查看只剩 1 条
- [ ] **关掉程序重开 → 任务还在**（持久化！）
- [ ] （加分）输入 abc 类乱输入不崩溃

## 七、完成标准

- 6 个功能全通 + 测试清单全过
- 用上了 class + 文件 + FILE_NAME 常量
- 重启后数据还在
