# 第 6 周 · 第 1 课：Matplotlib 数据可视化

## 一、为什么需要可视化？
- **数字看不出的规律，图表一眼就懂**
- 例：15 个商品的价格列表 → 看不出什么；画成柱状图 → 谁贵谁便宜一目了然
- **数据分析的最终交付物就是图表**（老板/客户只看图，不看代码）

## 二、基本流程（4 步）

```python
import matplotlib.pyplot as plt

# ① 准备数据
x = ["苹果", "香蕉", "西瓜"]
y = [5.5, 3.2, 15.0]

# ② 画图
plt.bar(x, y)

# ③ 加说明（标题、坐标轴）
plt.title("水果价格")
plt.xlabel("商品")
plt.ylabel("价格（元）")

# ④ 显示
plt.show()
```

## 三、三种基础图（按用途选）

| 图表 | 函数 | 用途 | 例子 |
|------|------|------|------|
| **折线图** | `plt.plot(x, y)` | 看**趋势**（随时间变化）| 每月销售额 |
| **柱状图** | `plt.bar(x, y)` | 比较**大小** | 各商品价格、各类别销量 |
| **散点图** | `plt.scatter(x, y)` | 看**关系** | 价格 vs 销量 |

```python
plt.plot(x, y)          # 折线
plt.bar(x, y)           # 柱状
plt.scatter(x, y)       # 散点
```

## 四、常用设置（让图能看懂）

```python
plt.title("标题")                    # 图标题
plt.xlabel("X 轴名称")               # X 轴标签
plt.ylabel("Y 轴名称")               # Y 轴标签
plt.legend()                        # 显示图例（多个数据系列时用）
plt.grid(True)                      # 显示网格（便于读数）
plt.xticks(rotation=45)             # X 轴文字旋转 45 度（防重叠！）
plt.figure(figsize=(10, 6))         # 设置图片大小（宽, 高）英寸
plt.tight_layout()                  # 自动调整布局，防止标签被裁掉
```

**多个数据系列**（要加 label 才能显示图例）：
```python
plt.plot(x, y1, label="2025年")
plt.plot(x, y2, label="2026年")
plt.legend()                        # 显示图例
```

## 五、⚠️ 中文显示问题（必设！否则中文变方块）

matplotlib 默认字体不支持中文，直接画中文会出现 `□□□` 方块。
**在代码最开头加这两行**：

```python
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]      # 用黑体显示中文
plt.rcParams["axes.unicode_minus"] = False        # 正常显示负号
```

（`SimHei` 是 Windows 自带的黑体；Mac 可用 `Arial Unicode MS`）

## 六、保存图片

```python
plt.savefig("价格图.png", dpi=150)     # 保存（要在 show() 之前！）
plt.show()
```
- `dpi=150`：分辨率（越高越清晰，文件也越大）
- ⚠️ **savefig 必须在 show() 之前**，否则保存的是空白图！

## 七、和 Pandas 结合（实战用法）

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("商品数据.csv", encoding="utf-8")

# 方式 1：直接用列名画
plt.bar(df["商品名称"], df["价格"])

# 方式 2：先 groupby 再画（分析常用！）
grouped = df.groupby("类别")["销量"].sum()
plt.bar(grouped.index, grouped.values)
```

## 八、画多张图（子图）

```python
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)      # 1行2列，第1张
plt.bar(x, y)
plt.title("图1")

plt.subplot(1, 2, 2)      # 1行2列，第2张
plt.scatter(x, y)
plt.title("图2")

plt.tight_layout()
plt.show()
```

## 九、记忆口诀

> plot 折线看趋势，bar 柱状比大小，scatter 散点找关系；
> title/xlabel/ylabel 三件套，legend 图例 grid 网格；
> 中文必设 SimHei，savefig 要在 show 前。

## 十、常见坑

| 坑 | 解决 |
|----|------|
| 中文显示成方块 | 开头设 `font.sans-serif = ["SimHei"]` |
| 保存的图是空白 | `savefig` 必须在 `show()` **之前** |
| X 轴文字挤成一团 | `plt.xticks(rotation=45)` |
| 标签被裁掉 | `plt.tight_layout()` |
| 图太小看不清 | `plt.figure(figsize=(10, 6))` |
| 忘记 plt.show() | 图画了但不显示（在脚本里必须写）|
