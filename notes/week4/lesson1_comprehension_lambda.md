# 第 4 周 · 第 1 课：进阶语法（列表推导式 + lambda）

## 一、列表推导式 —— 把"循环+append"缩成 1 行

### 回忆你以前的写法（3 行）：
```python
result = []
for x in numbers:           # 遍历
    result.append(x * 2)    # 加工后存进新列表
```

### 列表推导式（1 行）：
```python
result = [x * 2 for x in numbers]
```

**格式模板**：
```python
[对 x 做什么  for x in 列表]
```

### 加条件过滤（2 合 1）：
```python
# 以前：
result = []
for x in numbers:
    if x >= 60:              # 只要及格的
        result.append(x)

# 推导式：
result = [x for x in numbers if x >= 60]
```

**完整格式**：
```python
[对 x 做什么  for x in 列表  if 条件]
```

### 更多例子：
```python
nums = [1, 2, 3, 4, 5]

[x ** 2 for x in nums]            # [1, 4, 9, 16, 25] 平方
[str(x) for x in nums]            # ['1','2','3','4','5'] 转字符串
[x for x in nums if x % 2 == 0]   # [2, 4] 只要偶数
```

### 用在字典上（你的成绩系统！）：
```python
students = {"小明": 92, "小红": 58, "小刚": 76}

# 找出所有及格学生的名字：
passed = [name for name, score in students.items() if score >= 60]
# ['小明', '小刚']

# 把所有成绩加 5 分：
new_scores = [score + 5 for score in students.values()]
# [97, 63, 81]
```

## 二、lambda —— 一行小函数（匿名函数）

### 对比 def：
```python
# def 写法（有名有姓，多行）：
def double(x):
    return x * 2

# lambda 写法（没名字，一行）：
double = lambda x: x * 2
```

**格式**：
```python
lambda 参数: 返回值
```

### lambda 最常见的用途：排序时当"钥匙"

sorted 可以按"某个规则"排序，lambda 就是那个规则：

```python
students = {"小明": 92, "小红": 58, "小刚": 76}

# 按成绩（值）从小到大排序：
sorted(students.items(), key=lambda x: x[1])
# [('小红', 58), ('小刚', 76), ('小明', 92)]
#                    ↑ x 是每个键值对，x[1] 是成绩

# 按姓名（键）排序：
sorted(students.items(), key=lambda x: x[0])
# [('小明', 92), ('小刚', 76), ('小红', 58)]
```

**拆解**：`sorted(列表, key=规则)` —— key 告诉 sorted "按什么排"，
lambda x: x[1] 就是说"按每个元素的第 1 个位置（成绩）排"。

### lambda 的注意点：
- 只能写一行，不能有 if/for 多行逻辑
- 用处就两个：① 排序 key ② 配 map/filter
- 复杂逻辑还是用 def！

## 三、map / filter（了解即可，见到认识）

```python
nums = [1, 2, 3, 4]

# map：把函数批量应用到每个元素
list(map(lambda x: x * 2, nums))     # [2, 4, 6, 8]

# filter：过滤（保留返回 True 的）
list(filter(lambda x: x > 2, nums))  # [3, 4]
```

⚠️ Python 3 里 map/filter 返回"迭代器"，要用 list() 包一下才能看到列表。

**其实……map/filter 能用列表推导式替代，更直观**：
```python
[x * 2 for x in nums]              # 代替 map
[x for x in nums if x > 2]         # 代替 filter
```
所以推导式更常用，map/filter 认识即可！

## 四、记忆口诀

> 推导式一行：对 x 做什么 for x in 列表 if 条件；
> lambda 一行函数：参数冒号返回值，排序 key 最常用；
> sorted 加 key，lambda 定规则；
> map 批量算，filter 筛一筛（推导式都能替）。

## 五、什么时候用推导式（判断标准）

**看得懂、一行能写完 → 用推导式**
**逻辑复杂超过一行 → 老老实实用 for 循环**
（代码是给人看的，可读性第一！）
