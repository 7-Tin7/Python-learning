# ============================================
# 第 6 周 练习 1：商品数据可视化 📊
#
# 用第 5 周的商品数据，画出 3 张图！
# 💡 这就是数据分析报告里的"图表部分"
#
# 新知识：Matplotlib（柱状图 / 散点图 / 中文设置 / 保存图片）
# 旧知识：Pandas（read_csv / groupby）
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# ---- 必设：中文显示（不加这行，中文会变方块）----
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
df = pd.read_csv("商品数据.csv", encoding="utf-8")

# ---- TODO 1：柱状图 —— 每个商品的价格 ----
# plt.figure(figsize=(10, 5))                    # 设置图片大小
# plt.bar(df["商品名称"], df["价格"])              # 柱状图
# plt.title("各商品价格对比")                      # 标题
# plt.xlabel("商品名称")                           # X 轴
# plt.ylabel("价格（元）")                          # Y 轴
# plt.xticks(rotation=45)                         # X 轴文字旋转，防重叠
# plt.grid(True, alpha=0.3)                       # 网格（alpha=透明度）
# plt.tight_layout()                              # 自动调整布局
# plt.savefig("图1_商品价格.png", dpi=150)         # 保存（在 show 之前！）
# plt.show()                                      # 显示

# ---- TODO 2：柱状图 —— 各类别的总销量（groupby！）----
# grouped = df.groupby("类别")["销量"].sum()       # 分类汇总
# plt.figure(figsize=(8, 5))
# plt.bar(grouped.index, grouped.values)          # index 是类别名，values 是数值
# plt.title("各类别总销量")
# plt.xlabel("类别")
# plt.ylabel("总销量")
# plt.savefig("图2_类别销量.png", dpi=150)
# plt.show()

# ---- TODO 3：散点图 —— 价格 vs 销量（看有没有关系）----
# plt.figure(figsize=(8, 5))
# plt.scatter(df["价格"], df["销量"])
# plt.title("价格与销量的关系")
# plt.xlabel("价格（元）")
# plt.ylabel("销量")
# plt.grid(True, alpha=0.3)
# plt.savefig("图3_价格与销量.png", dpi=150)
# plt.show()

# ---- 挑战（可选）：把 3 张图画在一张大图里（子图）----
# plt.figure(figsize=(15, 4))
# plt.subplot(1, 3, 1)
# plt.bar(df["商品名称"], df["价格"])
# plt.title("商品价格"); plt.xticks(rotation=90)
# plt.subplot(1, 3, 2)
# plt.bar(grouped.index, grouped.values)
# plt.title("类别销量")
# plt.subplot(1, 3, 3)
# plt.scatter(df["价格"], df["销量"])
# plt.title("价格 vs 销量")
# plt.tight_layout()
# plt.show()

# 运行后检查：
#   1. 会弹出 3 个图表窗口
#   2. 当前目录会生成 3 个 png 图片文件
#   3. 中文正常显示（不是方块 □□□）
#
# 💡 观察结论（可以写进分析报告）：
#   散点图能看出"价格高的商品销量是否更低"——这就是数据洞察！
# ============================================
