# -*- coding: utf-8 -*-
"""
第 6.6 单元 · 第 1 课 用：在 Linux 里跑起来的第一个 Python 脚本
==================================================================
⚠️ 特意写成【只用标准库】——不 import pandas / matplotlib。
   原因：Linux 里不一定装了这些包。先保证"一定能跑通"，
   跑通之后再考虑装包（见任务清单里的进阶任务）。

用法（在 WSL / Linux 终端里）：
    python3 hello_linux.py

或者把输出存进文件（重定向，第 1 课的必学操作）：
    python3 hello_linux.py > 报告/hello输出.txt
"""
import os
import platform
import socket
import sys

print("=" * 56)
print("  hello from Linux —— 证明我的脚本真在 Linux 里跑")
print("=" * 56)

# ── 第一部分：这台机器是谁 ──────────────────────────────
print()
print("【这台机器是谁】")
print("  操作系统   ：", platform.system(), platform.release())
print("  详细版本   ：", platform.version()[:60])
print("  Python 版本：", sys.version.split()[0])
print("  Python 在哪：", sys.executable)
print("  主机名     ：", socket.gethostname())

# ── 第二部分：我在哪个目录 ──────────────────────────────
print()
print("【我在哪】")
print("  当前目录   ：", os.getcwd())
print("  家目录     ：", os.path.expanduser("~"))
print("  当前用户   ：", os.environ.get("USER") or os.environ.get("USERNAME") or "?")

# ⭐ 判断是不是 Linux：Windows 上跑会打印 False
print("  是 Linux 吗：", platform.system() == "Linux")

# ── 第三部分：环境变量（对比 Windows 的图形界面）──────
print()
print("【环境变量 PATH 拆开看】")
path = os.environ.get("PATH", "")
# Windows 用 ; 分隔，Linux 用 : 分隔 —— 这也是个区别
sep = ";" if os.name == "nt" else ":"
parts = [p for p in path.split(sep) if p]
print(f"  共 {len(parts)} 条：")
for i, p in enumerate(parts[:6], 1):
    print(f"    {i}. {p}")
if len(parts) > 6:
    print(f"    ... 还有 {len(parts) - 6} 条")

# ── 第四部分：干点正事 —— 读数据、算个结果 ─────────────
print()
print("【干点正事：算一下这周的销售额】")
# ⚠️ 数据直接写在代码里，不依赖外部文件（保证一定能跑）
一周销售 = [
    ("周一", 1280.5),
    ("周二", 940.0),
    ("周三", 1732.5),
    ("周四", 1120.0),
    ("周五", 2050.5),
    ("周六", 3180.0),
    ("周日", 2465.5),
]

总计 = 0.0
最高日 = 一周销售[0]
for 星期, 金额 in 一周销售:
    总计 += 金额
    print(f"  {星期}   {金额:>10.2f}")
    if 金额 > 最高日[1]:
        最高日 = (星期, 金额)

平均 = 总计 / len(一周销售)
print("  " + "-" * 20)
print(f"  合计   {总计:>10.2f}")
print(f"  日均   {平均:>10.2f}")
print(f"  最高   {最高日[0]}  {最高日[1]:.2f}")

# ── 第五部分：收尾 ──────────────────────────────────────
print()
print("=" * 56)
print("  跑完啦。这段输出就是任务清单里的【对账目标】之一。")
print("=" * 56)
