# ============================================
# 第 5 周 练习 3：商品数据分析 🛒（Pandas 首秀！）
#
# 💡 这就是你兴趣目标 ①「爬商品信息分析」的核心流程：
#    读取数据 → 侦察 → 筛选 → 统计 → 分组 → 存结果
#    以后把 read_csv 换成"爬虫抓下来的数据"，就是真实项目！
#
# 数据文件：商品数据.csv（15 个商品，5 列）
#
# 新知识：Pandas（DataFrame / read_csv / 筛选 / groupby）
# 旧知识：布尔索引思路（NumPy 学过）、f-string
# ============================================

import pandas as pd

# ---- TODO 1：读取数据 ----
# df = pd.read_csv("商品数据.csv", encoding="utf-8")
# print(df)                     # 打印整张表看看

# ---- TODO 2：侦察数据 ----
# print(df.head())              # 前 5 行
# print(f"形状：{df.shape}")     # (15, 5)
# print(df.columns)             # 列名
# print(df.info())              # 每列类型 + 有无缺失值

# ---- TODO 3：选列 ----
# print(df["商品名称"])                          # 选一列（Series）
# print(df[["商品名称", "价格"]])                 # 选多列（双层括号！）

# ---- TODO 4：筛选 ----
# 价格大于 10 的商品：
#   expensive = df[df["价格"] > 10]
#   print(expensive)
# 类别是"水果"的商品：
#   fruits = df[df["类别"] == "水果"]
#   print(f"水果类商品：\n{fruits}")

# ---- TODO 5：统计 ----
# print(f"平均价格：{df['价格'].mean():.2f} 元")
# print(f"最贵的商品：{df['价格'].max()} 元")
# print(f"总销量：{df['销量'].sum()}")

# ---- TODO 6：排序 ----
# 按价格从高到低，只看前 3 名：
# top3 = df.sort_values("价格", ascending=False).head(3)
# print(f"最贵的 3 个商品：\n{top3}")

# ---- TODO 7：新增列（销售额 = 价格 × 销量）----
# df["销售额"] = df["价格"] * df["销量"]
# print(df[["商品名称", "销售额"]])

# ---- TODO 8：分组统计（Pandas 最强功能！）----
# print("各类别的平均价格：")
# print(df.groupby("类别")["价格"].mean())
# print("各类别的总销量：")
# print(df.groupby("类别")["销量"].sum())

# ---- 挑战（可选）：把分析结果存成新文件 ----
# df.to_csv("分析结果.csv", encoding="utf-8-sig", index=False)

# 示例输出片段：
#   平均价格：13.99 元
#   各类别的平均价格：
#   类别
#   水果    25.74
#   蔬菜     3.60
#   零食    15.47
#   饮料    13.13
# ============================================
