# 第 5 周 · 第 2 课：Pandas —— 表格数据处理（Excel 的 Python 版）

## 一、Pandas 是干嘛的？

- 处理**表格数据**（有行、有列名），就像 Python 版的 Excel
- 能读写 **CSV / Excel 文件**——处理"真实数据"的入口
- 是数据分析师每天用的核心工具
- 底层基于 NumPy（你刚学的知识直接复用）

**和 NumPy 的关键区别**：NumPy 用位置索引 `scores[:, 0]`，
Pandas 用**列名** `df["价格"]` —— 直观得多！

## 二、两个核心对象

| 对象 | 是什么 | 类比 |
|------|--------|------|
| **DataFrame** | 一张表（多列）| Excel 的工作表 |
| **Series** | 一列数据 | Excel 的一列 |

```python
import pandas as pd          # 惯例简写 pd

df["价格"]        # 取出"价格"这一列 → Series
df                # 整个表 → DataFrame
```

## 三、读取文件（最常见的第一步！）

```python
import pandas as pd

df = pd.read_csv("商品数据.csv", encoding="utf-8")
# 中文文件建议加 encoding="utf-8"（或 "utf-8-sig" 防乱码）

df = pd.read_excel("数据.xlsx")      # 读 Excel（需装 openpyxl）
```

## 四、先"看看数据长什么样"（4 个侦察命令）

```python
df.head()        # 前 5 行（最常用！）
df.head(3)       # 前 3 行
df.tail()        # 后 5 行
df.shape         # (15, 5) 多少行多少列
df.info()        # 每列的类型、有没有缺失值
df.describe()    # 数值列的统计摘要（平均/最大/最小等）
df.columns       # 所有列名
```

## 五、选列

```python
df["价格"]                    # 选一列 → Series
df[["商品名称", "价格"]]       # 选多列 → DataFrame（注意是双层括号！）
```

## 六、筛选行（布尔索引，用列名！）

```python
df[df["价格"] > 10]                          # 价格大于 10 的商品
df[df["类别"] == "水果"]                      # 类别是水果的
df[(df["价格"] > 10) & (df["类别"] == "水果")]  # 组合条件（括号 + &）
```

**和 NumPy 一模一样的思路**，只是把 `scores >= 60` 换成了 `df["价格"] > 10`。

## 七、统计

```python
df["价格"].mean()        # 平均价格
df["价格"].max()         # 最贵
df["价格"].min()         # 最便宜
df["销量"].sum()         # 总销量
df["价格"].describe()    # 一揽子统计（个数/均值/四分位/最大最小）
```

## 八、排序

```python
df.sort_values("价格")                        # 按价格升序（便宜在前）
df.sort_values("价格", ascending=False)        # 降序（贵在前）
df.sort_values("销量", ascending=False).head(3)  # 销量前 3 名
```

## 九、新增列（超实用！）

```python
df["销售额"] = df["价格"] * df["销量"]     # 整列一起算（向量化！）
df["是否高价"] = df["价格"] > 20            # 生成 True/False 列
```

## 十、分组统计 groupby（Pandas 最强功能）⭐

```python
df.groupby("类别")["价格"].mean()     # 每个类别的平均价格
df.groupby("类别")["销量"].sum()      # 每个类别的总销量
df.groupby("类别").size()             # 每个类别有几个商品
```

**读法**：`按什么分组[对哪列做统计].统计函数()`
**意义**：从"一堆明细"里提炼出"分类汇总"——这就是"分析"的核心动作！

## 十一、保存结果

```python
df.to_csv("分析结果.csv", encoding="utf-8-sig", index=False)
# index=False：不要行号那一列
# utf-8-sig：Excel 打开中文不乱码
```

## 十二、记忆口诀

> read_csv 读进来，head 先看一眼；
> df["列名"] 取一列，双层括号取多列；
> 筛选就是 df[条件]，groupby 分类算；
> 新列直接赋值算，to_csv 存结果。

## 十三、常见坑

| 坑 | 说明 |
|----|------|
| 文件路径不对 | 要写对 CSV 的路径（同目录可直接写文件名）|
| 中文乱码 | 读加 `encoding="utf-8"`，存用 `encoding="utf-8-sig"` |
| 选多列只写一层括号 | `df["a","b"]` ❌ → 要 `df[["a","b"]]` ✅ |
| 组合条件忘了括号 | `df[df["价格"]>10 & df["类别"]=="水果"]` ❌ → 每个条件加括号 |
| 以为 df["价格"] 是列表 | 它是 Series，能用 .mean() 但和列表不完全一样 |
