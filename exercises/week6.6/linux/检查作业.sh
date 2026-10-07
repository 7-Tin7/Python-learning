#!/usr/bin/env bash
# ============================================================================
# 第 6.6 单元 · 第 1 课 Linux —— 作业自动检查脚本
# ============================================================================
# 用法（在 Linux 终端里，任何目录都行）：
#     bash 检查作业.sh
#
# 它做的事：逐条检查你的成果，每条给 ✅ 或 ❌。一共 19 条。
#   ✅ = 做对了    ❌ = 还没做 / 做错了（后面「期望」写了该怎么做）
#
# ⚠️ 这个脚本【只检查、不修改】。它不会帮你建目录、不会帮你拷文件。
#
# 💡 顺便说一句：这个文件本身就是一份不错的 bash 教材——
#    它用到了：变量、函数、if/elif/else、for、命令替换 $()、
#    文件测试（-f -d -x）、grep 的退出码、&& 和 || 短路。
#    你学完后可以回头看一遍，会很有收获。
# ============================================================================

WORK="$HOME/work/week6.6"
TOTAL=0
PASS=0
FAIL=0
EXPECT_N=""      # 正确答案（下面从你的日志里数出来，不写死）
LOG_A="$WORK/日志/服务日志_0918.txt"
LOG_B="$WORK/日志/服务日志_0919.txt"
BAK="$WORK/备份/服务日志_0919.txt.bak"
HELLO_OUT="$WORK/报告/hello输出.txt"

# ════════════════════════════════════════════════════════════
# 第一部分：记账工具
# ════════════════════════════════════════════════════════════

# 每调用一次 chk，就多一条成绩（这样总数永远等于 chk 的调用次数）
chk() {
    # 用法：chk "描述" "期望提示" 判定函数名
    desc="$1"
    hint="$2"
    fn="$3"
    TOTAL=$((TOTAL + 1))
    if "$fn"; then
        PASS=$((PASS + 1))
        echo "  ✅ 第 $TOTAL 条  $desc"
    else
        FAIL=$((FAIL + 1))
        echo "  ❌ 第 $TOTAL 条  $desc"
        echo "        └─ 期望：$hint"
    fi
}

# ════════════════════════════════════════════════════════════
# 第二部分：19 个判定函数
#   ⚠️ 必须写在 chk 调用【之前】—— bash 是逐行往下执行的，
#      函数得先被定义，后面才能调用。（这本身就是个知识点）
# ════════════════════════════════════════════════════════════

# ── 第一组：目录结构 ──
c_work()      { [ -d "$WORK" ]; }
c_subdirs()   { [ -d "$WORK/日志" ] && [ -d "$WORK/备份" ] && [ -d "$WORK/报告" ]; }

# ── 第二组：日志目录 ──
c_two_logs()  { [ -f "$LOG_A" ] && [ -f "$LOG_B" ]; }
c_log_count() { [ "$(find "$WORK/日志" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')" = "2" ]; }
c_line20()    { [ "$(wc -l < "$LOG_A" 2>/dev/null | tr -d ' ')" = "20" ]; }

# ── 第三组：备份与删除 ──
c_bak()       { [ -f "$BAK" ]; }
c_bak_same()  { cmp -s "$BAK" "$LOG_B" 2>/dev/null; }
c_temp_gone() { [ ! -f "$WORK/原始/temp_待删.txt" ]; }

# ── 第四组：统计结果 ──
c_count_ok()  { [ -n "$EXPECT_N" ] && [ "$(grep -o '[0-9]\+' "$WORK/报告/错误行数.txt" 2>/dev/null | head -1)" = "$EXPECT_N" ]; }
c_detail_n()  { [ -n "$EXPECT_N" ] && [ "$(wc -l < "$WORK/报告/错误明细.txt" 2>/dev/null | tr -d ' ')" = "$EXPECT_N" ]; }
c_detail_all(){ [ -s "$WORK/报告/错误明细.txt" ] && ! grep -qv "ERROR" "$WORK/报告/错误明细.txt" 2>/dev/null; }

# ── 第五组：跑 Python ──
c_hello_py()  { [ -f "$WORK/hello_linux.py" ]; }
c_hello_out() { [ -f "$HELLO_OUT" ]; }
c_is_linux()  { grep -q "是 Linux 吗： True" "$HELLO_OUT" 2>/dev/null; }
c_has_total() { grep -q "合计" "$HELLO_OUT" 2>/dev/null; }

# ── 第六组：自己写的脚本 ──
c_sh_exists() { [ -f "$WORK/统计.sh" ]; }
c_sh_exec()   { [ -x "$WORK/统计.sh" ]; }
c_sh_runs()   { bash "$WORK/统计.sh" >/dev/null 2>&1; }
c_sh_num()    { [ -n "$EXPECT_N" ] && [ "$(bash "$WORK/统计.sh" 2>/dev/null | grep -o '[0-9]\+' | head -1)" = "$EXPECT_N" ]; }

# ════════════════════════════════════════════════════════════
# 第三部分：开跑
# ════════════════════════════════════════════════════════════

echo "============================================================"
echo "   第 6.6 单元 · 第 1 课 Linux 作业检查"
echo "   检查位置：$WORK"
echo "============================================================"

if [ ! -d "$WORK" ]; then
    echo
    echo "❌ 找不到 $WORK"
    echo
    echo "   第 1 条任务就是建它："
    echo "       mkdir -p ~/work/week6.6"
    echo
    echo "   结果：0 / 19 条通过。做完再来跑一次。"
    exit 1
fi

# 从日志里数出正确答案（不写死数字）
if [ -f "$LOG_A" ] && [ -f "$LOG_B" ]; then
    EXPECT_N=$(grep -h "ERROR" "$LOG_A" "$LOG_B" | wc -l | tr -d ' ')
fi

echo
echo "── 第一组：目录结构 ──"
chk "工作目录 ~/work/week6.6 存在" \
    "mkdir -p ~/work/week6.6" \
    c_work
chk "日志 / 备份 / 报告 三个子目录都在" \
    "cd ~/work/week6.6 && mkdir -p 日志 备份 报告" \
    c_subdirs

echo
echo "── 第二组：文件整理（日志目录）──"
chk "两个真日志都在 日志/ 里（0918 + 0919）" \
    "cp 原始/服务日志_0918.txt 原始/服务日志_0919.txt 日志/" \
    c_two_logs
chk "日志/ 里【恰好】2 个文件，没混进杂物" \
    "别把 说明.txt / 备份_* / temp_* 拷进来" \
    c_log_count
chk "服务日志_0918.txt 内容完整（20 行）" \
    "用 cp 原样拷，不要手改内容" \
    c_line20

if [ -d "$WORK/日志" ] && ! c_log_count; then
    echo "        └─ 现在 日志/ 里是："
    find "$WORK/日志" -maxdepth 1 -type f -printf "             %f\n" 2>/dev/null
fi

echo
echo "── 第三组：备份 与 删除 ──"
chk "备份/服务日志_0919.txt.bak 存在（改名做对了）" \
    "cp 原始/备份_服务日志_0919.txt 备份/服务日志_0919.txt.bak" \
    c_bak
chk "备份内容和原文件【完全一致】（逐字节对比）" \
    "用 cp 拷，别手改内容" \
    c_bak_same
chk "原始/temp_待删.txt 已删除" \
    "rm 原始/temp_待删.txt（先 ls 确认再删）" \
    c_temp_gone

echo
echo "── 第四组：统计结果（grep 的真本事）──"
chk "报告/错误行数.txt 内容正确" \
    "bash 统计.sh > 报告/错误行数.txt" \
    c_count_ok
chk "报告/错误明细.txt 行数正确" \
    "grep ERROR 日志/*.txt > 报告/错误明细.txt" \
    c_detail_n
chk "错误明细里每行都含 ERROR（是 grep 出来的，不是手抄的）" \
    "直接重定向 grep 的输出，别手动整理" \
    c_detail_all

echo
echo "── 第五组：在 Linux 里跑 Python ⭐ ──"
chk "hello_linux.py 已拷进工作目录" \
    "cp 课材料/hello_linux.py .（结尾的 . 表示当前目录）" \
    c_hello_py
chk "报告/hello输出.txt 存在（重定向 > 用对了）" \
    "python3 hello_linux.py > 报告/hello输出.txt" \
    c_hello_out
chk "输出证明脚本跑在 Linux 里（「是 Linux 吗： True」）" \
    "这个文件必须是在 Linux 里跑出来的，不是从 Windows 拷的" \
    c_is_linux
chk "输出里有销售统计结果（说明 5 个部分都跑完了）" \
    "先在屏幕上跑通：python3 hello_linux.py" \
    c_has_total

echo
echo "── 第六组：自己写的脚本 + 可执行权限 ⭐⭐ ──"
chk "统计.sh 存在（自己写的脚本）" \
    "nano 统计.sh 写一个；用 grep 数 ERROR 行数" \
    c_sh_exists
chk "统计.sh 有【可执行权限】" \
    "chmod +x 统计.sh，再用 ls -l 看开头有没有 x" \
    c_sh_exec
chk "统计.sh 能跑通（没报错）" \
    "常见原因：没写 #!/bin/bash，或路径写错" \
    c_sh_runs
chk "统计.sh 输出的数字正确" \
    "脚本里对 日志/ 目录做 grep 统计" \
    c_sh_num

if c_sh_exists && ! c_sh_num; then
    echo "        └─ 你的脚本输出是：$(bash "$WORK/统计.sh" 2>&1 | head -3)"
fi

# ════════════════════════════════════════════════════════════
# 第四部分：成绩单
# ════════════════════════════════════════════════════════════

echo
echo "============================================================"
echo "   成绩：$PASS / $TOTAL 条通过"
echo "============================================================"

if [ "$FAIL" -eq 0 ]; then
    echo
    echo "  🎉🎉 全绿！第 1 课 Linux 作业全部通过。"
    echo
    echo "  你已经能独立完成：导航 / 建目录 / 拷文件 / 改名 / 删文件 /"
    echo "  看内容 / 搜索 / 改权限 / 重定向 / 在 Linux 里跑 Python / 写 bash 脚本。"
    echo
    echo "  把这份输出贴给我，我们做避坑总结。"
else
    echo
    echo "  还有 $FAIL 条没过。别急，按 ❌ 后面的「期望」一条条来。"
    echo "  改完再跑一次：bash 检查作业.sh"
fi
echo
exit 0
