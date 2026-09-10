# 第 3 周 · 第 2 课：文件读写（open / with）

## 一、为什么需要文件
你的成绩管理系统最大的遗憾：**程序一关，数据全没了**。
文件（.txt / .csv / .json）就是"硬盘上的仓库"——程序关了，数据还在，
下次启动还能读回来。这就是【持久化】。

## 二、写文件（三件套：打开 → 写入 → 关闭）

```python
f = open("成绩.txt", "w", encoding="utf-8")   # ① 打开（w=写入模式）
f.write("小明 92\n")                            # ② 写入（\n 是换行）
f.close()                                       # ③ 关闭（必须！）
```

⚠️ 三个要点：
1. **"w" 模式会清空原文件再写**（覆盖！）
2. **encoding="utf-8" 必须写**！否则写中文会报错（Windows 默认编码不认中文）
3. **用完必须 close()**——忘了关可能数据没真正存进硬盘

## 三、with 语句 —— 自动关闭（最推荐！）

```python
with open("成绩.txt", "w", encoding="utf-8") as f:
    f.write("小明 92\n")
    f.write("小红 85\n")
# 缩进结束后，文件【自动关闭】，不用写 close()
```

with = "用完自动关"，再也不会忘。以后都用 with！

## 四、读文件

```python
with open("成绩.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 全部内容 → 一个大字符串
    # 或者
    lines = f.readlines()       # 每行一个元素 → 列表
    # 或者最常用：直接 for 遍历每一行
    for line in f:
        print(line.strip())     # strip() 去掉每行末尾的换行符 \n
```

## 五、三种模式速查

| 模式 | 含义 | 文件不存在时 | 会覆盖原内容吗 |
|------|------|------------|--------------|
| "r" | 读 | 报错 FileNotFoundError | - |
| "w" | 写 | 自动创建 | ✅ 会清空重写 |
| "a" | 追加 | 自动创建 | ❌ 不清空，接在末尾写 |

## 六、实战：成绩系统的"保存/加载"思路（周项目预告）

保存（把字典写成文件）：
```python
with open("成绩.txt", "w", encoding="utf-8") as f:
    for name, score in contacts.items():
        f.write(f"{name} {score}\n")   # 每行 "姓名 成绩"
```

加载（把文件读回字典）：
```python
contacts = {}
with open("成绩.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(" ")   # "小明 92" → ["小明", "92"]
        contacts[parts[0]] = int(parts[1])
```

【拆开理解】line = "小明 92\n" → strip 去 \n → "小明 92" → split(" ") 按空格拆
→ ["小明", "92"] → parts[0] 是姓名，parts[1] 是成绩（字符串）→ int() 转数字

## 七、读不存在的文件会崩 → 用 try/except 接住（第 1 课联动！）

```python
try:
    with open("成绩.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:        # 文件还不存在
    print("还没有保存过数据")
```

## 八、记忆口诀

> open 打开，with 自动关；
> w 清空写，a 追加尾，r 只读看；
> encoding 写 utf-8，中文不乱码；
> 读文件要防 FileNotFoundError；
> 存字典一行一记录，读回来 split 再转换。
