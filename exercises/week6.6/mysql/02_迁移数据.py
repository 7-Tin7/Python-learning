# -*- coding: utf-8 -*-
"""
第 6.6 单元 · 第 2 课 MySQL —— 任务：把 SQLite 的数据搬到 MySQL
==================================================================
运行：  D:\python\python.exe 02_迁移数据.py
依赖：  pip install pymysql cryptography

⚠️ 运行前必须先：
   ① 装好 pymysql（见上）
   ② 复制 db_config_示例.py → db_config.py，并填上你的 MySQL 密码
   ③ 跑过 01_建库建表.sql，两张表已经建好

━━━ 这一课的核心：两个数据库的【代码差异】在哪 ━━━
  第 6.5 单元的代码（SQLite）          第 6.6 单元的代码（MySQL）
  ────────────────────────────────────────────────────────────────
  sqlite3.connect("销售.db")      →   pymysql.connect(host=..., user=..., password=...)
   （一个文件，不要账号密码）           （要主机+端口+用户+密码，因为是服务端）

  游标占位符用  ?                 →   游标占位符用  %s
   （sqlite3 的写法）                    （pymysql 的写法）⚠️ 容易搞混！

  conn.commit()                   →   conn.commit()
   （一样）                              （一样）

  ⭐ SQL 语句本身：几乎不用改！
     这就是这一课最想让你体验到的：换数据库，不用重学 SQL。
"""
import os
import sqlite3
import sys

# ── 读配置：没有 db_config.py 就给出清晰指引（不报一堆看不懂的错）──
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
try:
    import db_config as cfg
except ImportError:
    print("=" * 66)
    print("❌ 找不到 db_config.py")
    print("=" * 66)
    print()
    print("   请先做这一步（只做一次）：")
    print("     ① 把 db_config_示例.py 复制一份，改名为 db_config.py")
    print("     ② 打开它，把 password 改成你的 MySQL 密码")
    print()
    print("   命令行做法：")
    print("     copy db_config_示例.py db_config.py")
    print()
    sys.exit(1)

# 检查占位符是否还是模板里的原话（提醒他别忘了改密码）
if "在这里填" in cfg.MYSQL.get("password", ""):
    print("=" * 66)
    print("⚠️  db_config.py 里的密码还没改，现在还是模板文字。")
    print("=" * 66)
    print()
    print('   请把 "password" 改成你自己的 MySQL root 密码。')
    print()
    sys.exit(1)

import pymysql   # 放在配置检查之后 import，这样没装包时也能看到友好提示
                  # （⚠️ 其实这里 import 失败还是会报 ImportError，
                  #   要更优雅可以包 try/except，你可以自己试试改）


# ══════════════════════════════════════════════════════════════
# 两张表的列（顺序必须和 MySQL 建表时一致，否则数据会串列！）
# ══════════════════════════════════════════════════════════════
订单列 = ["订单编号", "日期", "商品名称", "类别", "单价", "数量", "城市", "月份", "销售额"]
成本列 = ["商品名称", "成本价", "供应商"]


def 读sqlite(表名, 列名列表):
    """从 SQLite 读一张表（这段已经写好了，不用改）"""
    conn = sqlite3.connect(cfg.SQLITE_PATH)
    cur = conn.cursor()
    sql = "SELECT " + ",".join(列名列表) + " FROM " + 表名
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    print(f"  📖 从 SQLite 读到 {表名}：{len(rows)} 行")
    return rows


def 写mysql(表名, 列名列表, rows):
    """把数据写进 MySQL —— ⭐ 这一段要你补完

    ✅ 目标：打印出插入了几行
    ✅ 别忘了 commit()，否则数据不落库（和 SQLite 的规矩一样）
    ⚠️ 占位符是 %s，不是 ? —— 这是 pymysql 的写法
    """
    # ① 连上 MySQL（⚠️ 要指定 database，因为库已经建好了）
    conn = pymysql.connect(
        host=cfg.MYSQL["host"],
        port=cfg.MYSQL["port"],
        user=cfg.MYSQL["user"],
        password=cfg.MYSQL["password"],
        database=cfg.DB_NAME,          # ← 指定库名
        charset="utf8mb4",
    )
    cur = conn.cursor()

    # ② 拼出 INSERT 语句
    #    ⚠️ 反引号包住中文列名，最保险
    #    目标长这样：INSERT INTO `订单` (`订单编号`,`日期`,...) VALUES (%s,%s,...)
    #
    # TODO(1)：把下面这行补完（提示：用 列名列表 拼出列名部分和 %s 部分）
    #   %s 的个数要和列数一样多，可以用  ",".join(["%s"] * len(列名列表))
    sql = "TODO"

    # ③ 批量插入
    # TODO(2)：用 cur.executemany(sql, rows) 插入，然后 conn.commit()
    #

    print(f"  ✍️  写入 MySQL {表名}：{len(rows)} 行")

    # ④ 关连接（好习惯）
    cur.close()
    conn.close()


def main():
    print("=" * 66)
    print("  把 销售.db 的数据迁到 MySQL")
    print("=" * 66)
    print(f"  SQLite 源文件：{cfg.SQLITE_PATH}")
    print(f"  文件存在吗    ：{os.path.exists(cfg.SQLITE_PATH)}")
    print(f"  MySQL 目标    ：{cfg.MYSQL['host']}:{cfg.MYSQL['port']} / 库 {cfg.DB_NAME}")
    print()

    # ── 先做一次"能连上吗"的体检（省得后面一堆报错分不清原因）──
    print("【第 0 步】测试能不能连上 MySQL")
    try:
        conn = pymysql.connect(
            host=cfg.MYSQL["host"], port=cfg.MYSQL["port"],
            user=cfg.MYSQL["user"], password=cfg.MYSQL["password"],
            charset="utf8mb4",
        )
        cur = conn.cursor()
        cur.execute("SELECT VERSION()")
        print("  ✅ 连接成功！MySQL 版本：", cur.fetchone()[0])
        cur.execute("SHOW DATABASES LIKE %s", (cfg.DB_NAME,))
        if cur.fetchone():
            print(f"  ✅ 库 {cfg.DB_NAME} 存在")
        else:
            print(f"  ❌ 库 {cfg.DB_NAME} 不存在 —— 先跑 01_建库建表.sql")
            sys.exit(1)
        cur.close()
        conn.close()
    except pymysql.err.OperationalError as e:
        print("  ❌ 连不上 MySQL：", e)
        print()
        print("  逐条排查：")
        print("   ① 密码对不对？（db_config.py 里那个）")
        print("   ② MySQL 服务在跑吗？PowerShell 敲：")
        print("        Get-Service MySQL80")
        print("   ③ 装 pymysql 时有没有一起装 cryptography？")
        print("        pip install pymysql cryptography")
        sys.exit(1)

    # ── 第 1 步：读 SQLite ──
    print()
    print("【第 1 步】从 SQLite 读数据")
    订单数据 = 读sqlite(cfg.TABLE_ORDER, 订单列)
    成本数据 = 读sqlite(cfg.TABLE_COST, 成本列)

    # ── 第 2 步：写 MySQL ──
    print()
    print("【第 2 步】写进 MySQL")
    try:
        写mysql(cfg.TABLE_ORDER, 订单列, 订单数据)
        写mysql(cfg.TABLE_COST, 成本列, 成本数据)
    except pymysql.err.ProgrammingError as e:
        print("  ❌ SQL 写错了：", e)
        print("     检查：表建好了吗？列名对得上吗？%s 的个数对不对？")
        sys.exit(1)
    except TypeError as e:
        print("  ❌ 很可能是 sql 还是字符串 'TODO'，没补完：", e)
        sys.exit(1)

    # ── 第 3 步：验证 ──
    print()
    print("【第 3 步】验证（✅ 对账目标：订单 40 行 / 商品成本 11 行）")
    conn = pymysql.connect(
        host=cfg.MYSQL["host"], port=cfg.MYSQL["port"], user=cfg.MYSQL["user"],
        password=cfg.MYSQL["password"], database=cfg.DB_NAME, charset="utf8mb4",
    )
    cur = conn.cursor()
    for 表 in (cfg.TABLE_ORDER, cfg.TABLE_COST):
        cur.execute(f"SELECT COUNT(*) FROM `{表}`")
        实际 = cur.fetchone()[0]
        print(f"  MySQL 里 {表}：{实际} 行")
    # 顺手抽查一条，确认中文没乱码
    cur.execute(f"SELECT `订单编号`,`商品名称`,`类别`,`销售额` FROM `{cfg.TABLE_ORDER}` LIMIT 3")
    print("  抽查前 3 行（⚠️ 重点看中文有没有变成 ??? 或乱码）：")
    for r in cur.fetchall():
        print("     ", r)
    cur.close()
    conn.close()

    print()
    print("=" * 66)
    print("  迁移完成！下一步跑 03_交叉验证.py，")
    print("  让同一批 SQL 在 SQLite 和 MySQL 里各跑一遍，数字必须一样。")
    print("=" * 66)


if __name__ == "__main__":
    main()
