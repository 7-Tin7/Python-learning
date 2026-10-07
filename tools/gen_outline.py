# -*- coding: utf-8 -*-
r"""生成 notes\学习计划大纲_第1-20周.txt（从计划文件自动提取）
   简化版：只提取 [标题行] + [复选框行] + [打卡表]，保证健壮
   可重复运行
"""
import os
import re

BASE = r"E:\DeepseekHarness"
SRC = os.path.join(BASE, "Python-AI学习计划.md")
OUT = os.path.join(BASE, r"notes\学习计划大纲_第1-20周.txt")

t = open(SRC, encoding="utf-8").read()
行 = t.split("\n")
标题 = 行[0].replace("# 🎯 ", "").strip()

out = []
out.append("=" * 56)
out.append("学习计划大纲（离线速查版）")
out.append("=" * 56)
out.append("计划全称：" + 标题)
out.append("生成方式：从 Python-AI学习计划.md 自动提取")
out.append("          （计划更新后重新运行生成脚本即可，永不脱节）")
out.append("生成时间：2026-09-27")
out.append("")
out.append("本文件是【进度速查】。完整说明见：")
out.append("  · Python-AI学习计划.md        完整计划")
out.append("  · notes\\语法卡片速查表.txt     语法格式模板")
out.append("  · notes\\求职准备清单.txt       岗位/简历/面试")
out.append("  · notes\\JD样本库.txt           真实 JD 证据（8 样本）")
out.append("")

跳过章节 = ("三、学习资源推荐", "四、求职方向与定位",
            "五、我的个性化兴趣目标", "六、每周打卡表",
            "一、整体路径图")

跳过中 = False   # 是否处于"整节跳过"模式
for L in 行:
    s = L.rstrip()
    # 顶层 ## 标题：决定是否进入跳过模式
    if re.match(r"^## ", s):
        文本 = s.lstrip("#").strip()
        跳过中 = any(文本.startswith(k) for k in 跳过章节)
        if not 跳过中 and not 文本.startswith("二、"):
            # 保留"执行模式/双轨/备用区"等前置章节
            pass
        if 跳过中:
            continue
    if 跳过中:
        continue
    if re.match(r"^#{1,4} ", s):
        文本 = s.lstrip("#").strip()
        if s.startswith("# "):
            continue
        out.append("")
        out.append("-" * 56)
        out.append(文本)
        out.append("-" * 56)
    elif s.strip().startswith("- ["):
        标记 = "[x]" if "- [x]" in s else "[ ]"
        内容 = re.sub(r"^\s*- \[[ x]\]\s*", "", s)
        out.append("  " + 标记 + " " + 内容)
    elif s.strip().startswith("**") and s.strip().endswith("**") and len(s) < 80:
        out.append("  " + s.strip())

out.append("")
out.append("-" * 56)
out.append("每周打卡表")
out.append("-" * 56)
在表 = False
for L in 行:
    if L.startswith("| 周数"):
        在表 = True
        continue
    if 在表:
        if L.startswith("|---"):
            continue
        if L.startswith("|"):
            列 = [c.strip() for c in L.strip("|").split("|")]
            out.append("  " + " | ".join(列[:3]))
        else:
            在表 = False

out.append("")
out.append("=" * 56)
out.append("【下次从这里继续】")
out.append("  第 6.5 周 · 第 2 课：聚合与分组（GROUP BY / HAVING）")
out.append("    读：notes\\week6.5\\第2课_聚合与分组.md")
out.append("    做：exercises\\week6.5\\sql_practice_2.py（9 题）")
out.append("    对账基准：40 单 / 8148.60 元 / 客单价 203.72；水果 4502.1")
out.append("  之后：第 6.6 单元（Linux / MySQL / JS 基础）")
out.append("=" * 56)

新 = "\n".join(out) + "\n"
open(OUT, "w", encoding="utf-8", newline="\n").write(新)

print("生成成功")
print("  路径:", OUT)
print("  行数:", 新.count("\n"))
print()
print("=== 提取到的章节 ===")
for i, L in enumerate(out):
    if i > 0 and out[i - 1].startswith("-" * 56) and not L.startswith("-"):
        print("  ", L)
