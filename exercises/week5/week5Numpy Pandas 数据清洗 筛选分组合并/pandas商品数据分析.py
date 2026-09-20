import pandas as pd

print("1.读取数据")
df = pd.read_csv("商品数据.csv",encoding = "utf-8")
print(f"打印表格{df}")

print("2.侦察数据")
print(f"打印头五行{df.head()}")
print(f"形状:{df.shape}")
print(f"列名:{df.columns}")
print(f"每列类型+有无缺失值:")    #df.info放到f-string里会返回一个None,建议单独一行
df.info()

print("3.选列")
print(f"选列{df["商品名称"]}")
print(f"选多列{df[["类别","价格"]]}")

print("4.筛选")
expensive = df[df["价格"] > 10]
print(f"打印价格大于10的商品:{expensive}")
fruits = df[df["类别"] == "水果"]
print(f"打印类别是水果的商品:{fruits}")

print("5.统计")
print(f"平均价格:{df["价格"].mean():.2f}元")
print(f"最贵的商品:{df["价格"].max()}元")
print(f"总销量:{df["销量"].sum()}")

print("6.排序")
top3 = df.sort_values("价格",ascending = False).head(3)
print(f"价格排名前三的商品:\n{top3}")
low3 = df.sort_values("销量",ascending = True).head(3)
print(f"销量最低的三个商品:\n{low3}")

print("7.新增列（销售额=价格*销量）")
df["销售额"] = df["价格"] * df["销量"]
print(df[["商品名称","销售额"]])

print("8.分组统计(pandas主要功能)")
print("各类别的平均价格:")
print(f"各类别的平均价格(保留两位小数)：\n{round(df.groupby("类别")["价格"].mean(),2)}")
print("各类别的平均销售额：")
print(f"各类别的平均销售额(保留两位小数)：\n{round(df.groupby("类别")["销售额"].mean(),2)}")
print("各类的总销量：")
print(f"各类别的总销量:\n{df.groupby("类别")["销量"].sum()}")

print("9.把分析结果存成新文件")
df.to_csv("分析结果.csv",encoding="utf-8-sig",index = False)    #index=False(不保存自动生成的序号)