# ============================================
# 🏆 周项目：电商销售数据分析
#
# 流程：侦察 → 清洗 → 分析 → 可视化 → 报告
# 数据：销售数据_原始.csv（47 行，含 5 类脏数据）
# 说明书：notes/week6/week_project_sales.md
#
# 建议分 3 次完成，不要一次写完！
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# 中文显示（必设）
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# ═══════════════════════════════════════
# 第 1 步：数据侦察（先看看数据有多脏）
# ═══════════════════════════════════════
df = pd.read_csv("销售数据_原始.csv", encoding="utf-8")

print("=" * 45)
print("【数据侦察】")
print(f"原始形状：{df.shape}")
print("\n前 5 行：")
print(df.head())
print("\n各列缺失值数量：")
print(df.isnull().sum())
print(f"\n重复行数：{df.duplicated().sum()}")
print(f"类别取值（看有没有多余空格）：{df['类别'].unique()}")
print(f"数量最小值（看有没有负数）：{df['数量'].min()}")

# TODO 1：自己再补几个侦察动作
#   · 看看单价的最小值（有没有 0 或负数）：print(df["单价"].min())
#   · 看看日期列的类型：print(df["日期"].dtype)
#   · 看看城市有哪些取值：print(df["城市"].unique())


# ═══════════════════════════════════════
# 第 2 步：数据清洗（本周核心！）
# ═══════════════════════════════════════
print("\n" + "=" * 45)
print("【数据清洗】")

# ---- TODO 2：删除重复行 ----
# before = len(df)
# df = df.drop_duplicates()
# print(f"删除重复行：{before} → {len(df)}")

# ---- TODO 3：处理缺失值 ----
# 关键字段（数量）缺失 → 删除该行
# df = df.dropna(subset=["数量"])
# 非关键字段（城市）缺失 → 填充"未知"
# df["城市"] = df["城市"].fillna("未知")
# print(f"处理后缺失值：\n{df.isnull().sum()}")

# ---- TODO 4：清理类别的多余空格（.str 访问器）----
# df["类别"] = df["类别"].str.strip()
# print(f"清洗后类别：{df['类别'].unique()}")     # 应该是 4 种

# ---- TODO 5：过滤异常值 ----
# df = df[df["数量"] > 0]        # 数量必须为正
# df = df[df["单价"] > 0]        # 单价必须大于 0
# print(f"过滤异常值后：{len(df)} 行")

# ---- TODO 6：类型转换 ----
# df["数量"] = df["数量"].astype(int)      # 转整数
# df["日期"] = pd.to_datetime(df["日期"])   # 转日期类型
# df["月份"] = df["日期"].dt.month          # 提取月份（.dt 访问器）
# print(f"日期类型：{df['日期'].dtype}")

# ⚠️ 检查点：此时应该满足
#    · 类别只有 4 种  · 无重复行  · 无负数量/0单价  · 日期是 datetime


# ═══════════════════════════════════════
# 第 3 步：数据分析
# ═══════════════════════════════════════
print("\n" + "=" * 45)
print("【数据分析】")

# ---- TODO 7：新增"销售额"列 ----
# df["销售额"] = df["单价"] * df["数量"]

# ---- TODO 8：关键指标 ----
# print(f"总销售额：{df['销售额'].sum():.2f} 元")
# print(f"总订单数：{len(df)}")
# print(f"平均客单价：{df['销售额'].mean():.2f} 元")

# ---- TODO 9：各类别销售额 ----
# by_category = df.groupby("类别")["销售额"].sum().sort_values(ascending=False)
# print(f"\n各类别销售额：\n{by_category}")

# ---- TODO 10：月度趋势 ----
# by_month = df.groupby("月份")["销售额"].sum()
# print(f"\n月度销售额：\n{by_month}")

# ---- TODO 11：城市排名 ----
# by_city = df.groupby("城市")["销售额"].sum().sort_values(ascending=False)
# print(f"\n城市销售额排名：\n{by_city}")

# ---- TODO 12：Top 5 商品 ----
# top5 = df.groupby("商品名称")["销售额"].sum().nlargest(5)
# print(f"\n销售额 Top 5 商品：\n{top5}")


# ═══════════════════════════════════════
# 第 4 步：可视化（4 张图）
# ═══════════════════════════════════════

# ---- TODO 13：图1 各类别销售额（柱状图）----
# by_category = df.groupby("类别")["销售额"].sum()
# plt.figure(figsize=(8, 5))
# plt.bar(by_category.index, by_category.values)
# plt.title("各类别销售额对比")
# plt.xlabel("类别"); plt.ylabel("销售额（元）")
# plt.grid(True, alpha=0.3); plt.tight_layout()
# plt.savefig("图1_类别销售额.png", dpi=150); plt.show()

# ---- TODO 14：图2 月度销售趋势（折线图，注意是 plot）----
# by_month = df.groupby("月份")["销售额"].sum()
# plt.figure(figsize=(8, 5))
# plt.plot(by_month.index, by_month.values, marker="o")
# plt.title("月度销售趋势"); plt.xlabel("月份"); plt.ylabel("销售额（元）")
# plt.xticks([1, 2, 3])          # 月份只显示 1/2/3
# plt.grid(True, alpha=0.3); plt.tight_layout()
# plt.savefig("图2_月度趋势.png", dpi=150); plt.show()

# ---- TODO 15：图3 城市销售额（横向柱状图 barh）----
# by_city = df.groupby("城市")["销售额"].sum().sort_values()
# plt.figure(figsize=(8, 5))
# plt.barh(by_city.index, by_city.values)    # ← barh 横着画，城市名更好看
# plt.title("各城市销售额"); plt.xlabel("销售额（元）")
# plt.grid(True, alpha=0.3); plt.tight_layout()
# plt.savefig("图3_城市销售额.png", dpi=150); plt.show()

# ---- TODO 16：图4 各类别占比（饼图）----
# by_category = df.groupby("类别")["销售额"].sum()
# plt.figure(figsize=(7, 7))
# plt.pie(by_category.values, labels=by_category.index,
#         autopct="%.1f%%", startangle=90)   # autopct 显示百分比
# plt.title("各类别销售额占比")
# plt.tight_layout()
# plt.savefig("图4_类别占比.png", dpi=150); plt.show()


# ═══════════════════════════════════════
# 第 5 步：输出报告（写进 README 或单独 txt）
# ═══════════════════════════════════════
# 参照说明书第六节的报告模板，写：
#   一、数据概况    二、清洗过程
#   三、核心发现    四、结论与建议  ← 最重要！
#
# 报告里每个结论都要有【数字支撑】，例如：
#   "饮料类销售额 XXX 元，占总额 XX%，为第一大类"
