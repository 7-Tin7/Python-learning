# ============================================
# 第 2 周 练习：句子加工厂（参考答案）🏭
# 每个知识点都标了注释，边读边回忆
# ============================================

# ---- TODO 1：获取输入并清洗 ----
raw = input("请输入一个英文句子（单词用空格隔开）：")
sentence = raw.strip()            # strip()：去掉首尾多余空格

# ---- TODO 2：显示基本信息 ----
print(f"句子长度：{len(sentence)}")      # len() 对字符串 = 字符个数
print(f"清洗后内容：{sentence}")

# ---- TODO 3：拆分成单词 ----
words = sentence.split()          # split() 不写参数 = 按空格拆 → 列表
print(f"单词列表：{words}")        # ['hello', 'world', 'python', 'is', 'fun!']
print(f"一共 {len(words)} 个单词")

# ---- TODO 4：切片截取 ----
print(f"第 1 个单词：{words[0]}")          # 列表也能用 [0] 取第一个
print(f"第 1 个单词的首字母：{words[0][0]}")  # [0][0]：先取单词，再取单词的第 0 个字符
print(f"最后 3 个字符：{sentence[-3:]}")     # 负数切片：从右边数 3 个

# ---- TODO 5：替换练习 ----
print(f"把 'o' 换成 '0'：{sentence.replace('o', '0')}")   # replace(旧, 新)
