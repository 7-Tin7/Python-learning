# 第 3 周 · 第 1 课：异常处理（try / except）

## 一、什么是"异常"（Exception）
程序运行时遇到的错误 = 异常。异常会【中断程序、直接崩溃】。
你这两周反复遇到的崩溃，全是异常：

```python
int("abc")        # ValueError：无法把 "abc" 转成数字
5 / 0             # ZeroDivisionError：除数不能为 0
d["不存在的键"]    # KeyError：字典里没有这个键
[1,2,3][99]       # IndexError：索引超出列表范围
```

## 二、try / except —— 让程序"摔倒了能爬起来"

```python
try:
    num = int(input("请输入数字："))   # 这行可能出错
except ValueError:                     # 出错时跳到这里
    print("输入的不是数字！")
# 程序继续运行，不会崩溃 ✅
```

执行流程：
1. 先执行 try 里的代码
2. 没出错 → 跳过 except，继续往下走
3. 出错了 → 立即跳到 except，执行 except 里的代码，然后继续走
4. 【关键】程序不会崩溃！

## 三、异常类型（按需捕捉）

| 异常 | 含义 | 常见触发 |
|------|------|---------|
| ValueError | 值错误 | int("abc") |
| ZeroDivisionError | 除零 | 5 / 0 |
| KeyError | 键不存在 | d["xxx"] |
| IndexError | 索引越界 | 列表[99] |
| TypeError | 类型错误 | "1" + 1 |

也可以拿到具体错误信息：
```python
try:
    x = int("abc")
except ValueError as e:      # as e：把错误信息存进变量 e
    print("出错原因：", e)    # 出错原因： invalid literal for int()...
```

## 四、else 和 finally（了解即可）

```python
try:
    num = int(input("数字："))
except ValueError:
    print("不是数字")
else:
    print(f"转换成功：{num}")    # 没出错才执行
finally:
    print("一定会执行")           # 无论出不出错都执行（常用于关闭文件）
```

## 五、两种"防御哲学"（重要！）

Python 社区有两种保护程序的方式：

| 方式 | 哲学 | 英文缩写 | 你会的例子 |
|------|------|---------|-----------|
| 先检查 | "过马路先看车" | LBYL | isdigit() 预检查 |
| 异常处理 | "先走，被撞了再处理" | EAFP | try/except |

两者各有优势：
- isdigit()：只能检查"纯数字"，但简单直观
- try/except：能拦截【任何】转换错误，连 "85.5"（小数）都能正确处理

```python
# isdigit 写法（你会了）
s = input("成绩：")
if not s.isdigit():
    print("请输入数字")

# try/except 写法（这课学的）—— 配合 float 还能接受小数！
try:
    score = float(input("成绩："))    # float 能吃 "85" 和 "85.5"
except ValueError:
    print("请输入数字")
```

## 六、黄金套路：安全输入函数（while + try/except）

想让程序"输入不对就重新问，直到对了为止"，用这个模式：

```python
def get_number(prompt):
    while True:                        # 问到你答对为止
        try:
            return float(input(prompt))    # 成功 → 直接返回
        except ValueError:                 # 失败 → 提示后重新循环
            print("输入的不是数字，请重新输入！")
```

调用：x = get_number("请输入第一个数：")   ← 永远返回合法数字，绝不崩溃！

## 七、记忆口诀

> try 试运行，except 接异常；
> 出错不崩溃，跳过去处理；
> as e 拿信息，else 无错跑；
> finally 兜底，关文件靠它；
> 安全输入函数：while + try 问到底。
