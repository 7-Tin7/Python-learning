# -*- coding: utf-8 -*-
r"""
第 6.5 单元 · 第 1 课 脚手架：建一个 SQLite 数据库

★ 开头的 r 是"原始字符串"：让 \p \D 这类反斜杠不被当成转义字符。
  写 Windows 路径的文档字符串必须加 r，否则会报警告。
------------------------------------------------------------------
运行：  D:\python\python.exe db_setup.py   （在 week6.5 文件夹里运行）
作用：  把第 6 周清洗后的销售数据（40 行）装进数据库文件 销售.db

★ 这个文件不用你改，看懂就行。你今天的任务是 第1课_练习.py
★ 每次重跑它，都会把 销售.db 删掉重建，保证数据永远是干净的 40 行
"""
import csv
import os
import sqlite3

# ── 找路径（用绝对路径最稳，不受"你在哪个目录运行"影响）──────────
BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "..", "week6", "销售数据_清洗后.csv")
DB_PATH = os.path.join(BASE, "销售.db")

# ── ① 如果库文件已存在，先删掉（反复练习时不会数据翻倍）─────────
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# ── ② 连接数据库（文件不存在会自动创建，这是 SQLite 的好处）──────
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()          # cursor = 执行器，SQL 都要靠它去跑

# ── ③ 建表：先规定好"表里有哪些列、每列存什么类型"────────────────
#    TEXT=文字  INTEGER=整数  REAL=小数
cursor.execute("""
CREATE TABLE 订单 (
    订单编号 TEXT,
    日期     TEXT,
    商品名称 TEXT,
    类别     TEXT,
    单价     REAL,
    数量     INTEGER,
    城市     TEXT,
    月份     INTEGER,
    销售额   REAL
)
""")

# ── ④ 读 CSV，整理成一批数据，一次性插入 ─────────────────────────
with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

data = [
    (
        r["订单编号"], r["日期"], r["商品名称"], r["类别"],
        float(r["单价"]), int(r["数量"]), r["城市"],
        int(r["月份"]), float(r["销售额"]),
    )
    for r in rows
]

# ? 是"占位符"，真正的值由后面的 data 按顺序填进去（防注入，也防引号出错）
cursor.executemany("INSERT INTO 订单 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

# ── ⑤ 建第二张表：商品成本（第 3 课 JOIN 用）─────────────────────
#    ⚠️ 故意【少了两个商品】（薯片、矿泉水）—— 这是有意的设计，
#       用来演示 LEFT JOIN 的效果（左表有、右表没有 → 显示 NULL）
cursor.execute("""
CREATE TABLE 商品成本 (
    商品名称 TEXT,
    成本价   REAL,
    供应商   TEXT
)
""")

成本数据 = [
    ("樱桃",   42.0, "山野果园"),
    ("咖啡",   22.0, "云南豆业"),
    ("西瓜",    9.5, "海南瓜田"),
    ("巧克力", 17.0, "甜心食品"),
    ("饼干",    8.0, "甜心食品"),
    ("香蕉",    2.1, "海南瓜田"),
    ("苹果",    3.6, "山野果园"),
    ("黄瓜",    2.2, "绿野蔬菜"),
    ("可乐",    2.3, "清爽饮料"),
    ("白菜",    1.5, "绿野蔬菜"),
    ("西红柿",  3.2, "绿野蔬菜"),
    # ⚠️ 注意：薯片、矿泉水【故意没有】——用来演示 LEFT JOIN
]
cursor.executemany("INSERT INTO 商品成本 VALUES (?, ?, ?)", 成本数据)

# ── ⑥ 提交！不 commit，插入的数据只活在内存里，关掉就没了 ────────
conn.commit()

# ── ⑦ 自检：数一数两张表各有多少行 ──────────────────────────────
cursor.execute("SELECT COUNT(*) FROM 订单")
订单数 = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM 商品成本")
成本数 = cursor.fetchone()[0]

print("建库完成 ：", DB_PATH)
print("表【订单】    ：", 订单数, "行")
print("表【商品成本】：", 成本数, "行（⚠️ 故意少了薯片、矿泉水，用于演示 LEFT JOIN）")
print()
print("提示：重跑本脚本会【删库重建】，两张表都会重置。")

conn.close()                    # 用完关掉
