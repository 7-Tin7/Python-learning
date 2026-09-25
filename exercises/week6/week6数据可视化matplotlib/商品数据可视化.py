"""笔记
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]    #中文用黑体表示
plt.rcParams["axes.unicode_minus"] = False      #负号正常显示
plt.bar(x,y)      #柱状图（比大小）
plt.plot(x,y)  #折线图，看趋势
plt.scatter(x,y)     #散点图（看关系）
plt.figure(figsize=(10,5))   #图片大小（宽，高）
plt.xticks(rotation=45)      #X轴文字旋转，防重叠
plt.savefig("图.png",dpi=150)   #必须在show()之前，否则存空白图
plt.title("标题")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.show("显示")"""


import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
df = pd.read_csv("商品数据.csv",encoding="utf-8")
plt.figure(figsize=(10,5))
plt.bar(df["商品名称"],df["价格"])
plt.title("各商品价格对比")
plt.xlabel("商品名称")
plt.ylabel("价格（元）")
plt.xticks(rotation=45)
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("图1_商品价格.png",dpi=150)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("商品数据.csv",encoding="utf-8")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
grouped = df.groupby("类别")["销量"].sum()
plt.figure(figsize = (10,5))
plt.bar(grouped.index,grouped.values)
plt.title("各类别总销量")
plt.xlabel("类别")
plt.ylabel("总销量")
plt.xticks(rotation=45)
plt.grid(True,alpha=0.3)
plt.savefig("图2_类别销售.png",dpi=150)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
df = pd.read_csv("商品数据.csv",encoding="utf-8")
plt.figure(figsize=(10,5))
plt.scatter(df["价格"],df["销量"])
plt.title("价格vs销量")
plt.xlabel("价格")
plt.ylabel("销量")
plt.tight_layout()
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.savefig("图3.散点图.png",dpi=150)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
df = pd.read_csv("商品数据.csv",encoding="utf-8")
grouped = df.groupby("类别")["销量"].sum()
plt.figure(figsize=(10,5))
plt.subplot(1,3,1)
plt.bar(df["商品名称"],df["价格"])
plt.title("各商品价格对比")
plt.xticks(rotation=45)
plt.subplot(1,3,2)
plt.bar(grouped.index,grouped.values)
plt.title("各类别总销量")
plt.grid(True,alpha=0.3)
plt.subplot(1,3,3)
plt.scatter(df["价格"],df["销量"])
plt.title("价格vs销量")
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig("图4.三子图和一.png",dpi=150)
plt.show()

grouped = df.groupby("类别")["销量"].agg(["count","sum","mean"])
tmp = grouped.reset_index()
print(tmp)






