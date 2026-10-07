# -*- coding: utf-8 -*-
"""
第 6.6 单元 · 第 2 课 MySQL —— 交叉验证：同一批 SQL，两边各跑一遍
==================================================================
运行：  D:\python\python.exe 03_交叉验证.py
依赖：  pip install pymysql cryptography  +  已跑过 01/02

━━━ 这个脚本是干什么的（⭐ 本课最重要的习惯）━━━
  把【同一批 SQL】分别丢给 SQLite 和 MySQL，然后逐条对比结果。
  · 数字一样  → ✅ 说明你的 SQL 是对的，而且换数据库真的不用重学
  · 数字不一样 → ❌ 必有一边错了（或两边都错）

  这就是你在第 6.5 单元用过的【交叉验证】——
  当时你靠它发现了 8.0 那个差异。现在换个场景继续用：
  ⭐ 一个查询在两个地方算出来不一样 → 必有一处是错的。

⚠️ 关于"结果的类型"（重要，别被它骗了）
  SQLite 的 ROUND() 返回 float；MySQL 的 ROUND() 返回 Decimal。
      SQLite: 4477.1      MySQL: Decimal('4477.10')
  这【不是错】，是两个数据库对"精确小数"的态度不同
  （MySQL 更严谨，因为 DECIMAL 是给钱用的）。
  所以本脚本比较前会先【归一化】：数字统一按数值比，日期统一按字符串比。
  真正的类型差异，我在最后单独列出来给你看 —— 那是本课的重点之一。
"""
import os
import sqlite3
import sys
from decimal import Decimal

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)

try:
    import db_config as cfg
except ImportError:
    print("❌ 找不到 db_config.py，请先按 02_迁移数据.py 的提示复制一份并填密码。")
    sys.exit(1)

try:
    import pymysql
except ImportError:
    print("❌ 没装 pymysql。请在命令行运行：")
    print("     D:\\python\\python.exe -m pip install pymysql cryptography")
    sys.exit(1)


# ══════════════════════════════════════════════════════════════
# 要交叉验证的查询清单（这些 SQL 两边都能跑，语法几乎一样）
#   ⭐ 注意：这里写的 SQL 用反引号包中文列名 —— 两边都认。
# ══════════════════════════════════════════════════════════════
QUERIES = [
    ("订单总行数", "SELECT COUNT(*) FROM `订单`"),
    ("商品成本行数", "SELECT COUNT(*) FROM `商品成本`"),
    ("城市去重数", "SELECT COUNT(DISTINCT `城市`) FROM `订单`"),
    ("总销售额", "SELECT ROUND(SUM(`销售额`), 2) FROM `订单`"),
    ("按类别销售额",
     "SELECT `类别`, ROUND(SUM(`销售额`), 2) AS s FROM `订单` GROUP BY `类别` ORDER BY s DESC"),
    ("按类别订单数",
     "SELECT `类别`, COUNT(*) AS n FROM `订单` GROUP BY `类别` ORDER BY n DESC"),
    ("按城市销售额 top3",
     "SELECT `城市`, ROUND(SUM(`销售额`), 2) AS s FROM `订单` "
     "GROUP BY `城市` ORDER BY s DESC LIMIT 3"),
    ("INNER JOIN 行数（对账 38）",
     "SELECT COUNT(*) FROM `订单` INNER JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称`"),
    ("LEFT JOIN 行数（对账 40）",
     "SELECT COUNT(*) FROM `订单` LEFT JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称`"),
    ("各商品毛利润（11 行）",
     "SELECT `订单`.`商品名称`, ROUND(SUM(`订单`.`销售额`), 2) AS 销售额, "
     "ROUND(SUM(`订单`.`数量` * `商品成本`.`成本价`), 2) AS 总成本, "
     "ROUND(SUM(`订单`.`销售额` - `订单`.`数量` * `商品成本`.`成本价`), 2) AS 毛利润 "
     "FROM `订单` INNER JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称` "
     "GROUP BY `订单`.`商品名称` ORDER BY 毛利润 DESC"),
    ("毛利润总额（对账 2687.3）",
     "SELECT ROUND(SUM(`订单`.`销售额` - `订单`.`数量` * `商品成本`.`成本价`), 2) "
     "FROM `订单` INNER JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称`"),
    ("按供应商毛利润",
     "SELECT `供应商`, ROUND(SUM(`订单`.`销售额` - `订单`.`数量` * `商品成本`.`成本价`), 2) AS p "
     "FROM `订单` INNER JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称` GROUP BY `供应商` ORDER BY p DESC"),
    ("成本表里缺失的商品（应为 矿泉水/薯片）",
     "SELECT DISTINCT `订单`.`商品名称` FROM `订单` LEFT JOIN `商品成本` "
     "ON `订单`.`商品名称` = `商品成本`.`商品名称` WHERE `商品成本`.`商品名称` IS NULL"),
    ("跨类别的商品（上次修完应为空）",
     "SELECT `商品名称`, COUNT(DISTINCT `类别`) FROM `订单` "
     "GROUP BY `商品名称` HAVING COUNT(DISTINCT `类别`) > 1"),
]


def 归一化(v):
    """把值转成可比较的字符串（数字按数值比，日期按文本比）"""
    if v is None:
        return "NULL"
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, (int, float, Decimal)):
        f = float(v)
        if f == int(f):
            return str(int(f))
        return str(round(f, 4))
    return str(v)


def 规范化结果(rows):
    """结果标准化成一个可比较的"集合形式"（忽略行的先后顺序，只比内容和行数）"""
    return sorted(tuple(归一化(c) for c in row) for row in rows)


def 连sqlite():
    conn = sqlite3.connect(cfg.SQLITE_PATH)
    return conn


def 连mysql():
    return pymysql.connect(
        host=cfg.MYSQL["host"], port=cfg.MYSQL["port"], user=cfg.MYSQL["user"],
        password=cfg.MYSQL["password"], database=cfg.DB_NAME, charset="utf8mb4",
    )


def main():
    print("=" * 74)
    print("  交叉验证：同一批 SQL，SQLite 与 MySQL 各跑一遍")
    print("=" * 74)
    print(f"  SQLite : {cfg.SQLITE_PATH}")
    print(f"  MySQL  : {cfg.MYSQL['host']}:{cfg.MYSQL['port']} / {cfg.DB_NAME}")
    print()

    # ── 建立两个连接 ──
    try:
        sq = 连sqlite()
    except sqlite3.Error as e:
        print("❌ 连不上 SQLite：", e)
        sys.exit(1)
    if not os.path.exists(cfg.SQLITE_PATH):
        print(f"❌ 找不到 {cfg.SQLITE_PATH}")
        print("   重跑建库脚本：D:\\python\\python.exe exercises\\week6.5\\db_setup.py")
        sys.exit(1)

    try:
        my = 连mysql()
    except pymysql.err.OperationalError as e:
        print("❌ 连不上 MySQL：", e)
        print("   ① 密码对不对（db_config.py）  ② MySQL80 服务在跑吗  ③ 01/02 跑过吗")
        sys.exit(1)

    sq_cur = sq.cursor()
    my_cur = my.cursor()

    print("─" * 74)
    print(f"{'查询':<34}{'SQLite':>10}{'MySQL':>10}   结果")
    print("─" * 74)

    通过 = 0
    失败 = 0
    明细差异 = []

    for 标题, sql in QUERIES:
        try:
            sq_cur.execute(sql)
            sq_rows = sq_cur.fetchall()
            sq_err = None
        except Exception as e:
            sq_rows, sq_err = None, e

        try:
            my_cur.execute(sql)
            my_rows = my_cur.fetchall()
            my_err = None
        except Exception as e:
            my_rows, my_err = None, e

        sq_n = "报错" if sq_err else f"{len(sq_rows)} 行"
        my_n = "报错" if my_err else f"{len(my_rows)} 行"

        if sq_err or my_err:
            print(f"{标题:<34}{sq_n:>10}{my_n:>10}   ❌ 有一边报错了")
            失败 += 1
            明细差异.append((标题, f"SQLite 报错: {sq_err}", f"MySQL 报错: {my_err}"))
            continue

        if 规范化结果(sq_rows) == 规范化结果(my_rows):
            print(f"{标题:<34}{sq_n:>10}{my_n:>10}   ✅ 完全一致")
            通过 += 1
        else:
            print(f"{标题:<34}{sq_n:>10}{my_n:>10}   ❌ 不一致！")
            失败 += 1
            明细差异.append((标题, sq_rows, my_rows))

    print("─" * 74)
    print(f"  结果：{通过} 条一致 / {失败} 条不一致  （共 {len(QUERIES)} 条）")
    print("─" * 74)

    # ── 不一致的，把两边结果都打出来，方便定位 ──
    if 明细差异:
        print()
        print("=" * 74)
        print("  不一致的明细（两边结果对照）")
        print("=" * 74)
        for 标题, a, b in 明细差异:
            print()
            print(f"【{标题}】")
            print("  SQLite :")
            if isinstance(a, list):
                for r in a:
                    print("     ", r)
            else:
                print("     ", a)
            print("  MySQL  :")
            if isinstance(b, list):
                for r in b:
                    print("     ", r)
            else:
                print("     ", b)

    # ── 单独观察：类型差异（不参与上面的判定）──
    print()
    print("=" * 74)
    print("  【重点观察】同样的值，两个数据库返回的 Python 类型不一样")
    print("=" * 74)
    print("  这不是错——是两个数据库的设计不同。看清楚它们的差别：")
    print()
    观察SQL = [
        ("日期字段", "SELECT `日期` FROM `订单` LIMIT 1"),
        ("金额字段", "SELECT `销售额` FROM `订单` LIMIT 1"),
        ("ROUND 结果", "SELECT ROUND(SUM(`销售额`), 2) FROM `订单`"),
    ]
    for 名字, sql in 观察SQL:
        sq_cur.execute(sql)
        v1 = sq_cur.fetchone()[0]
        my_cur.execute(sql)
        v2 = my_cur.fetchone()[0]
        print(f"  {名字}")
        print(f"     SQLite → 值 {str(v1):<14} 类型 {type(v1).__name__}")
        print(f"     MySQL  → 值 {str(v2):<14} 类型 {type(v2).__name__}")
        print()

    # ── 单独观察：严格程度差异 ──
    print("=" * 74)
    print("  【重点观察】MySQL 比 SQLite 严格——这条 SQL 两边表现会不同")
    print("=" * 74)
    坏SQL = "SELECT `类别`, `月份`, ROUND(SUM(`销售额`), 2) FROM `订单` GROUP BY `类别`"
    print("  故意写一条『SELECT 里有非分组列』的 SQL：")
    print(f"     {坏SQL}")
    print()
    print("  回忆第 6.5 单元笔记里那句话：")
    print("     『SELECT 里只能放分组列 + 聚合函数（放了别的列不报错，但结果无意义）』")
    print("  ⚠️ 那是 SQLite 的行为。换成 MySQL 试试：")
    print()
    try:
        sq_cur.execute(坏SQL)
        print("  SQLite →", sq_cur.fetchall())
        print("           （⚠️ 它【没报错】，给了你一个毫无意义的结果）")
    except Exception as e:
        print("  SQLite → 报错：", e)
    try:
        my_cur.execute(坏SQL)
        print("  MySQL  →", my_cur.fetchall())
        print("           （⚠️ 咦，它也没报错？那把结果贴给我，我们分析）")
    except Exception as e:
        print("  MySQL  → 报错 ✅：", str(e)[:160])
        print("           （这就是 MySQL 8 默认开启的 ONLY_FULL_GROUP_BY 模式：")
        print("            非分组列必须用聚合函数包起来，否则直接拒绝执行）")

    # ── 收尾 ──
    print()
    print("=" * 74)
    if 失败 == 0:
        print("  🎉 全部一致！")
        print()
        print("  这说明两件事：")
        print("   ① 你的 SQL 是对的（两个引擎算出同一个数，几乎不可能是巧合）")
        print("   ② 你的数据搬迁是完整的（40/11 行一个不多一个不少）")
        print()
        print("  ⭐ 更重要的：你第 6.5 单元学的 SQL 语法，")
        print("     换到 MySQL 几乎一行都不用改 —— 这就是要你亲身体会的事。")
    else:
        print(f"  ❌ 有 {失败} 条不一致。按上面打印的两边结果对照，")
        print("     先想清楚『哪边对』，再找原因。找不出来就把明细贴给我。")
    print("=" * 74)

    sq_cur.close()
    sq.close()
    my_cur.close()
    my.close()


if __name__ == "__main__":
    main()
