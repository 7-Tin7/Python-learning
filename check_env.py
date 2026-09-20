import sys

print("=" * 50)
print("Python 环境体检报告")
print("=" * 50)
print(f"Python 版本: {sys.version.split()[0]}")
print(f"Python 路径: {sys.executable}")
print()

# 检查各个包的安装情况
packages = [
    ("numpy", "数值计算（第5周）"),
    ("pandas", "表格数据处理（第5周）"),
    ("openpyxl", "读 Excel 文件（第5周）"),
    ("matplotlib", "数据可视化（第6周）"),
    ("seaborn", "统计图形（第6周）"),
    ("requests", "爬虫 HTTP 请求（兴趣目标①）"),
    ("bs4", "网页解析 BeautifulSoup（兴趣目标①）"),
    ("sklearn", "机器学习 Scikit-learn（第7周）"),
]

print("【包安装情况】")
for name, desc in packages:
    try:
        mod = __import__(name)
        ver = getattr(mod, "__version__", "?")
        print(f"  [OK]      {name:12s} {ver:10s} - {desc}")
    except ImportError:
        print(f"  [未安装]  {name:12s} {'':10s} - {desc}")

print()
print("【功能实测】")

# 实测 1：pandas 能否读取 CSV
try:
    import pandas as pd
    df = pd.read_csv("商品数据.csv", encoding="utf-8")
    print(f"  [OK] pandas 成功读取商品数据.csv")
    print(f"       形状: {df.shape}  （{df.shape[0]} 行 × {df.shape[1]} 列）")
    print(f"       列名: {list(df.columns)}")
    print(f"       平均价格: {df['价格'].mean():.2f} 元")
except FileNotFoundError:
    print("  [注意] 找不到 商品数据.csv（请确认当前目录）")
except Exception as e:
    print(f"  [失败] {e}")

# 实测 2：NumPy 能否工作
try:
    import numpy as np
    a = np.array([1, 2, 3])
    print(f"  [OK] NumPy 运算正常（{a} + 10 = {a + 10}）")
except Exception as e:
    print(f"  [失败] {e}")

print()
print("=" * 50)
