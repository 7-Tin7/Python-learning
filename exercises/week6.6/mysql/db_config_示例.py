# -*- coding: utf-8 -*-
"""
第 6.6 单元 · 第 2 课 MySQL —— 连接配置【模板】
==================================================================
用法（两步）：
  ① 把本文件复制一份，改名为  db_config.py
        Windows 命令行：  copy db_config_示例.py db_config.py
        （或者在 PyCharm 里右键 → Copy → Paste，再改名）
  ② 打开 db_config.py，把 password 改成你自己的 MySQL 密码

⚠️⚠️ 为什么不能直接改这个文件？
   因为 db_config.py 已经被 .gitignore 排除，不会被推到 GitHub；
   而本文件（_示例）是要上传的，里面【绝对不能】有真密码。

   —— 这个思路就是"配置与代码分离"：
      代码可以公开，密码不能公开。
      第 7-11 周第 3 课会学正式的 .env 做法，比这个更规范。

⚠️ 密码忘记怎么办？
   装 MySQL 时设的那个 root 密码。如果真忘了，可以在
   MySQL 安装目录下找 my.ini，或用 MySQL Installer 重设。
   别急，先试试常见的几个（你注册时常用的密码）。
"""
import os

# ── MySQL 连接参数 ──────────────────────────────────────────
MYSQL = {
    "host": "127.0.0.1",        # 本机就是 127.0.0.1（localhost）
    "port": 3306,               # MySQL 默认端口（我们用 netstat 验证过）
    "user": "root",             # 用户名
    "password": "在这里填你的MySQL密码",   # ⚠️ 改成你自己的
    "charset": "utf8mb4",       # ⚠️ 必须是 utf8mb4，否则中文会乱码
}

# 注意：database 不写死在这里，因为建库前它还不存在。
# 建完库之后，脚本里用 MYSQL["database"] = "销售_db" 补上。

# ── SQLite 文件位置（第 6.5 单元那个库）────────────────────
# 从本文件（exercises/week6.6/mysql/）往回到 week6.5
BASE = os.path.dirname(os.path.abspath(__file__))
SQLITE_PATH = os.path.join(BASE, "..", "week6.5", "销售.db")
SQLITE_PATH = os.path.normpath(SQLITE_PATH)

# ── 统一的数据库名 / 表名（两个脚本共用，改一处就够）──────
DB_NAME = "销售_db"
TABLE_ORDER = "订单"
TABLE_COST = "商品成本"
