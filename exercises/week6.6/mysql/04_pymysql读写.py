# -*- coding: utf-8 -*-
"""
第 6.6 单元 · 第 2 课 MySQL —— 任务：用 Python 对 MySQL 做增删改查
==================================================================
运行：  D:\python\python.exe 04_pymysql读写.py
依赖：  pip install pymysql cryptography  +  已跑过 01/02

━━━ 本课的重点：占位符不一样 ⚠️ ━━━
  第 6.5 单元（sqlite3）：          本课（pymysql）：
      cur.execute("... WHERE 城市 = ?", ("上海",))     ← 用 ?
      cur.execute("... WHERE 城市 = %s", ("上海",))    ← 用 %s

  ⚠️ 这是最容易搞混的一处。写错会报
     "not enough arguments for format string" 之类的错。

━━━ 为什么要用占位符，不直接拼字符串？⚠️⚠️ 面试爱问 ━━━
  ❌ 危险写法：
     sql = "DELETE FROM `订单` WHERE `订单编号` = '" + 编号 + "'"
     —— 如果 编号 是  ' OR '1'='1
        拼出来就变成： WHERE 订单编号 = '' OR '1'='1'   → 删掉全表！
     这就是【SQL 注入】。

  ✅ 安全写法：
     cur.execute("DELETE FROM `订单` WHERE `订单编号` = %s", (编号,))
     —— 占位符由数据库驱动负责转义，用户输入永远只是"值"，不是"SQL 片段"
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
try:
    import db_config as cfg
except ImportError:
    print("❌ 找不到 db_config.py，请先复制 db_config_示例.py 并填密码。")
    sys.exit(1)
try:
    import pymysql
except ImportError:
    print("❌ 没装 pymysql，请运行：")
    print("     D:\\python\\python.exe -m pip install pymysql cryptography")
    sys.exit(1)


def 连上():
    return pymysql.connect(
        host=cfg.MYSQL["host"], port=cfg.MYSQL["port"], user=cfg.MYSQL["user"],
        password=cfg.MYSQL["password"], database=cfg.DB_NAME, charset="utf8mb4",
    )


def 打印(标题, rows, 列名=None):
    print(f"  {标题}")
    if 列名:
        print("     " + " | ".join(列名))
    for r in rows:
        print("     " + " | ".join(str(x) for x in r))
    print(f"     （{len(rows)} 行）")


def main():
    print("=" * 70)
    print("  用 pymysql 对 MySQL 做增删改查")
    print("=" * 70)
    conn = 连上()
    cur = conn.cursor()

    # ── 0. 先看看初始状态 ──
    cur.execute(f"SELECT COUNT(*) FROM `{cfg.TABLE_ORDER}`")
    print(f"\n【0】初始状态：订单表 {cur.fetchone()[0]} 行")

    # ══════════════════════════════════════════════════════════
    # 任务 1【增 INSERT】插一条测试订单进去
    #   用一条"一眼能认出来"的数据，方便待会儿删掉：
    #     订单编号 TEST0001 / 日期 2026-12-31 / 商品名称 测试商品
    #     类别 测试 / 单价 1.0 / 数量 1 / 城市 测试城 / 月份 12 / 销售额 1.0
    #
    #   ⚠️ 9 个值，9 个 %s，顺序必须和列名一模一样
    #   ⚠️ 插完必须 commit()，否则关掉程序就没了
    #
    #   ✅ 对账目标：插完 COUNT(*) 变成 41
    # ══════════════════════════════════════════════════════════
    print()
    print("【1】INSERT 插入一条测试订单")
    # TODO(1)：写 INSERT 语句（用 %s 占位符）
    sql_insert = "TODO"
    #
    # TODO(1b)：写要插入的 9 个值（元组）
    values_insert = ()
    #
    # TODO(1c)：执行 + commit，然后打印"已插入"
    #

    cur.execute(f"SELECT COUNT(*) FROM `{cfg.TABLE_ORDER}`")
    print(f"     插入后订单表 {cur.fetchone()[0]} 行（对账目标 41）")

    # ══════════════════════════════════════════════════════════
    # 任务 2【查 SELECT】把它查出来看看
    #   要求：只查刚插的那一条（WHERE `订单编号` = %s）
    # ✅ 对账目标：1 行；城市是"测试城"
    # ⚠️ 注意：即使只有 1 个参数，也要写成元组 —— ("TEST0001",)
    #    只写 ("TEST0001") 会被当成字符串而不是元组！
    #    ⚠️ 这就是你常犯的"少写一个逗号"类错误，注意看
    # ══════════════════════════════════════════════════════════
    print()
    print("【2】SELECT 查出来")
    # TODO(2)：执行查询并打印
    #

    # ══════════════════════════════════════════════════════════
    # 任务 3【改 UPDATE】把它改一下
    #   要求：把 城市 改成"改后城"、销售额 改成 999.99
    # ⚠️⚠️ 必须写 WHERE！不写 WHERE 会改【全表】（第 6.5 单元你亲手验证过）
    # ✅ 对账目标：cursor.rowcount 应为 1（影响 1 行）
    #    💡 记下 rowcount 这个属性：它告诉你"这条语句影响了几行"，
    #       是 SQL 作业里自查"我是不是改多了"的关键工具
    # ══════════════════════════════════════════════════════════
    print()
    print("【3】UPDATE 改一下")
    # TODO(3)：写 UPDATE + 执行 + commit + 打印 rowcount
    #

    # 再查一遍确认
    # TODO(3b)：查出来看看城市和销售额改了没有
    #

    # ══════════════════════════════════════════════════════════
    # 任务 4【删 DELETE】把测试数据删掉（⚠️ 保持数据库干净）
    #   要求：删掉 订单编号 = TEST0001 的那条
    #   ✅ 对账目标：删除后又变回 40 行（回到初始状态）
    # ══════════════════════════════════════════════════════════
    print()
    print("【4】DELETE 删掉测试数据")
    # TODO(4)：写 DELETE + 执行 + commit
    #

    cur.execute(f"SELECT COUNT(*) FROM `{cfg.TABLE_ORDER}`")
    print(f"     删除后订单表 {cur.fetchone()[0]} 行（对账目标 40）")

    # ══════════════════════════════════════════════════════════
    # 任务 5【参数化查询防注入 ⭐ 面试考点】
    #   下面的代码已经写好了，你只要运行并观察结果。
    #   它模拟"用户输入了一个恶意字符串"，看两种写法分别会发生什么。
    # ⚠️⚠️ 危险的那一半故意加了 .rollback() 兜底，
    #      但你在真实项目里千万别试！！
    # ══════════════════════════════════════════════════════════
    print()
    print("【5】SQL 注入演示（观察用，不用改）")
    恶意输入 = "' OR '1'='1"
    print(f"     模拟用户输入：{恶意输入}")
    print()

    # ⑤-1 危险写法：字符串拼接
    拼接SQL = f"SELECT COUNT(*) FROM `{cfg.TABLE_ORDER}` WHERE `城市` = '{恶意输入}'"
    print("     ❌ 拼接字符串的写法：")
    print(f"        拼出来的 SQL = {拼接SQL}")
    try:
        cur.execute(拼接SQL)
        条数 = cur.fetchone()[0]
        print(f"        查到 {条数} 行  ← {'⚠️⚠️ 全表都被匹配了！这就是注入' if 条数 > 0 else '（没匹配到）'}")
    except Exception as e:
        print("        报错：", e)

    # ⑤-2 安全写法：占位符
    print()
    print("     ✅ 用 %s 占位符的写法：")
    安全SQL = f"SELECT COUNT(*) FROM `{cfg.TABLE_ORDER}` WHERE `城市` = %s"
    print(f"        执行的 SQL = {安全SQL}")
    print(f"        参数       = {(恶意输入,)}")
    cur.execute(安全SQL, (恶意输入,))
    条数 = cur.fetchone()[0]
    print(f"        查到 {条数} 行  ← ✅ 它只被当成一个普通字符串，什么都没匹配到")

    print()
    print("     📌 结论：占位符让「用户输入」永远只是【值】，")
    print("        不可能变成【SQL 片段】。这就是参数化查询的全部意义。")

    # ── 收尾 ──
    conn.commit()
    cur.close()
    conn.close()
    print()
    print("=" * 70)
    print("  跑完啦。⚠️ 记得确认最后是 40 行——数据库要保持干净。")
    print("=" * 70)


if __name__ == "__main__":
    main()
