# 第 3 周 · 第 4 课：常用标准库（os / datetime）

> Python 自带很多"工具包"（标准库），这课学最常用的两个：
> os（操作系统文件管理）和 datetime（日期时间）

## 一、datetime —— 让程序"知道时间"

```python
from datetime import datetime        # 导入 datetime 类

now = datetime.now()                 # 当前这一刻
print(now)                           # 2025-01-15 14:30:45.123456
print(now.year)                      # 2025
print(now.month)                     # 1
print(now.day)                       # 15
```

### strftime：把时间格式化成字符串（最常用！）
```python
now.strftime("%Y-%m-%d %H:%M:%S")
# 结果："2025-01-15 14:30:45"
```

| 格式码 | 含义 | 例子 |
|--------|------|------|
| %Y | 四位年份 | 2025 |
| %m | 两位月份 | 01 |
| %d | 两位日 | 15 |
| %H | 小时(24h) | 14 |
| %M | 分钟 | 30 |
| %S | 秒 | 45 |

### 应用：日记自动加时间戳
```python
now = datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
f.write(f"[{time_str}] {note}\n")
# 写入： [2025-01-15 14:30:45] 今天学会了文件读写
```

## 二、os —— 操作系统文件管理

```python
import os

os.getcwd()                 # 当前程序在哪个文件夹
os.listdir()                # 这个文件夹里有哪些文件/文件夹（列表）
os.path.exists("a.txt")     # 文件存不存在（True/False）
os.path.getsize("a.txt")    # 文件多大（字节数）
os.remove("a.txt")          # 删除文件
os.rename("a.txt", "b.txt") # 重命名
```

### 应用 1：读文件前检查存在性
之前用 try/except 防 FileNotFoundError，现在有更直接的方式：
```python
if os.path.exists("日记.txt"):      # 存在才读
    with open("日记.txt", "r", encoding="utf-8") as f:
        ...
else:
    print("还没有日记")
```

### 应用 2：查看文件信息
```python
size = os.path.getsize("日记.txt")   # 返回字节数
print(f"日记文件大小：{size} 字节")
# 1 个汉字 ≈ 3 字节（utf-8）
```

## 三、什么时候用哪个？

| 需求 | 用哪个 |
|------|--------|
| 给记录加时间戳 | datetime.now().strftime |
| 检查文件存不存在 | os.path.exists |
| 知道文件多大 | os.path.getsize |
| 删除文件 | os.remove |
| 看文件夹里有什么 | os.listdir |
| 防"文件不存在"崩溃 | os.path.exists 或 try/except 都行 |

## 四、记忆口诀

> datetime 知时间，now 是现在，strftime 格式化；
> %Y%m%d 年月日，%H%M%S 时分秒；
> os 管文件，exists 查存在，getsize 看大小，remove 删文件。
