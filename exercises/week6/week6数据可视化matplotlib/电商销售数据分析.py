import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
df = pd.read_csv("销售数据_原始.csv",encoding="utf-8")
print("="*50)
print("第一步 侦察数据")
print("查看形状")
print(df.shape)
print("查看前五行")
print(df.head())
print("查看末尾五行")
print(df.tail())
print("查看缺失总值")
print(df.isnull().sum())
print("查看重复行数")
print(df.duplicated().sum())
print("unique:去除这一列所有不重复的值")
print(f"类别取值，查看是否有空格\n{df["类别"].unique()}")
print(f"数量最小值，查看是否有负数\n{df["数量"].min()}")
print(f"单价的最小值，查看是否有负数\n{df["单价"].min()}")
print(f"查看日期列的类型\n{df["日期"].dtype}")
print(f"查看城市有哪些取值\n{df["城市"].unique()}")

print("="*50)
print("第二步 数据清洗")
print("2.删除重复行")
before = len(df)
df = df.drop_duplicates()
print(f"去除重复行\n{before} ——> {len(df)}")

print("3.处理缺失值")
print("关键字段（数量）缺失——>删除这一行")
df = df.dropna(subset = ["数量"])
print(f"删除含有空值的内容，仅在数量这一列")
print("关键字段（城市）缺失——>填充（未知）  把空值替换成未知")
df["城市"] = df["城市"].fillna("未知")
print(f"处理后缺失值的数量\n{df.isnull().sum()}")

print("4.清理类别的多余空格")
print(f"删除字符串前后的空白字符")
df["类别"] = df["类别"].str.strip()
print(f"打印出清洗后类别所有不重复的值\n{df["类别"].unique()}")

print("5.过滤异常值")
df = df[df["数量"] > 0]
df = df[df["单价"] > 0]
print(f"过滤异常值后有{len(df)}行")

print("6.类型转换")
df["数量"] = df["数量"].astype(int)
print("把日期格式转换为pandas的日期类型，不转换无法提取")
df["日期"] = pd.to_datetime(df["日期"],format="mixed")
df["月份"] = df["日期"].dt.month
print(f"日期类型:{df['日期'].dtype}")

print("\n"+"="*45)
print("第三步 数据分析")
print("7.新增销售额列")
df["销售额"]=df["数量"] * df["单价"]

print("\n""8.关键指标")
print(f"总销售额:{df["销售额"].sum()}元")
print(f"总订单数:{len(df)}")
print(f"平均客单价:{df["销售额"].mean():.2f}元")

print("\n""9.各类别销售额")
by_category = df.groupby("类别")["销售额"].sum().sort_values(ascending=False)
print(f"各类别销售额排名从高到低{by_category}")

print("\n""10.月度趋势")
by_month = df.groupby("月份")["销售额"].sum()
print(f"月度销量趋势排名{by_month}")

print("\n""11.城市排名")
by_city = df.groupby("城市")["销售额"].sum().sort_values(ascending=False)
print(f"城市销售额排名{by_city}")

print("\n""12.商品排名")
goods = df.groupby("商品名称")["销售额"].sum().sort_values(ascending=False)
print(f"商品排名从高到低：{goods}")

print("第四步 可视化")
print("13.图一 各类别销售额（柱状图）")
by_category = df.groupby("类别")["销售额"].sum()
plt.figure(figsize=(10,7))
plt.bar(by_category.index,by_category.values)
plt.title("各类别销售额")
plt.xlabel("类别")
plt.ylabel("销售额")
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("图一.png",dpi=150)
plt.show()

print("14.图二 月度销售趋势（折线图）")
by_month = df.groupby("月份")["销售额"].sum()
plt.figure(figsize=(10,7))
plt.plot(by_month.index,by_month.values,marker="o")
plt.title("月度销售趋势")
plt.xlabel("月份")
plt.ylabel("销售额")
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("图二 月度销售趋势折线图.png",dpi=150)
plt.show()

print("15.图三 城市销售额横向柱状图")
by_city = df.groupby("城市")["销售额"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,7))
plt.barh(by_city.index,by_city.values)
plt.title("城市销售额")
plt.xlabel("销售额")
plt.ylabel("城市")
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("图三 城市销售额横向柱状图.png",dpi=150)
plt.show()

print("16.图四 各类别占比（饼图）")
by_category = df.groupby("类别")["销售额"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,7))
plt.pie(by_category.values,labels=by_category.index,autopct="%.1f%%",startangle=90)
plt.title("各类别占比图")
plt.tight_layout()
plt.savefig("图四 各类别占比.png",dpi=150)
plt.show()

"""总结：
     1.水果的销量最高，蔬菜的销量最低，可以注重打造水果产品，减少蔬菜产品的收购，甚至说可以抛弃蔬菜这一产品类别
     2.销量趋势从一月开始是峰值，到二月是峰谷，到三月又有显著上升，建议在一月和三月的时候加大产品的收购采入，在一月临近二月的时候逐步减少产品的收购，因为此时进入淡季，在二月到三月的时候逐步加大产品的采购，此时将迎来旺季，销量上升
     3.在深圳杭州北京广州的店铺可以加大产品的采购，这些城市的销售额数据都非常不错，可以减少在上海的店铺商品采购，甚至说关闭上海的店铺，因为在上海产品的销量一般，可以关闭店铺后重点打造销售额数据比较好的四个城市
     4.水果类别的销售额占比特别高，建议着重打造水果类别的产品，适当保持零食饮料类别的产品，可以舍弃掉占比特别少的蔬菜类产品"""